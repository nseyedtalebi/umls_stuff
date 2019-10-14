from os import environ
import json

import requests
from lxml.html import fromstring


class UMLSWebClient:
    CUSTOM_HEADER = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain", "User-Agent": "python"}
    AUTH_BASE = "https://utslogin.nlm.nih.gov"
    AUTH_ENDPOINT = "/cas/v1/api-key"
    API_BASE = "https://uts-ws.nlm.nih.gov/rest"

    def _get_tgt(self):
        params = {'apikey': self.apikey}
        r = requests.post(UMLSWebClient.AUTH_BASE + UMLSWebClient.AUTH_ENDPOINT,
                          data=params,
                          headers=UMLSWebClient.CUSTOM_HEADER
                          )
        response = fromstring(r.text)
        tgt = response.xpath('//form/@action')[0]
        return tgt

    def _get_st(self):
        params = {'service': self.service}
        r = requests.post(self.tgt, data=params, headers=UMLSWebClient.CUSTOM_HEADER)
        return r.text

    def _get_param_dict(self):
        return {"ticket": self._get_st()}

    def __init__(self, apikey=None, version="current"):
        self.service = "http://umlsks.nlm.nih.gov"
        self.version = version
        if apikey is not None:
            self.apikey = apikey
        else:
            self.apikey = environ['UMLS_API_KEY']
        assert(self.apikey is not None)
        self.tgt = self._get_tgt()
        assert(self.tgt is not None)

    '''
    HEY! The function below is currently BROKEN, but it was almost working.
    It returns None when it should have results...'''
    def crosswalk(self, code, source, target=None, page_number=1, page_size=25, page_limit=1):
        query_params = self._get_param_dict()
        if target is not None:
            query_params["targetSource"] = str(target)
        url = "{base}/crosswalk/{version}/source/{src}/{code}".format(
            base=UMLSWebClient.API_BASE,
            version=self.version,
            src=source,
            code=code,
        )
        results = []
        cur_page_number = page_number
        while True:
            query_params['pageNumber'] = cur_page_number
            query_params['pageSize'] = page_size
            r = requests.get(url, params=query_params)
            r.raise_for_status()
            r.encoding = 'utf-8'
            items = json.loads(r.text)
            json_data = items["result"]
            results.extend(json_data)
            if len(json_data) < page_size:
                break
            cur_page_number += 1
        return results

    def search(self, search_string, input_type="atom", include_obsolete=False, include_suppressible=False,
                      returnIdType="concept", sabs=None, search_type="words",
                      page_number=1, page_size=25, page_limit=1):
        url = self.API_BASE + "/search/" + self.version

        query_params = {
            'string': search_string,
            'inputType': input_type,
            'returnIdType': returnIdType,
            'searchType': search_type,
        }
        if sabs is not None:
            query_params['sabs'] = sabs
        query_params['includeObsolete'] = "true" if include_obsolete else "false"
        query_params['includeSuppressible'] = "true" if include_suppressible else "false"
        results = []
        cur_page_number = page_number
        while True:
            query_params['ticket'] = self._get_st()
            query_params['pageNumber'] = cur_page_number
            query_params['pageSize'] = page_size
            r = requests.get(url, params=query_params)
            r.raise_for_status()
            r.encoding = 'utf-8'
            items = json.loads(r.text)
            json_data = items["result"]
            results.extend(json_data["results"])
            if json_data["results"][0]["ui"] == "NONE" or cur_page_number > page_limit:
                break
            cur_page_number += 1
        return results

    def get_cui_from_ui(self, ui):
        url = "{base}/content/{vers}/CUI/{ui}".format(base=self.API_BASE, vers=self.version, ui=ui)
        query = self._get_param_dict()
        r = requests.get(url, params=query)
        r.encoding = 'utf-8'
        items = json.loads(r.text)
        return items["result"]

