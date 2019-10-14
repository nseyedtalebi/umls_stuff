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
        self.tgt = UMLSWebClient._get_tgt()
        assert(self.tgt is not None)

    def crosswalk(self, code, source, target):
        params = self._get_param_dict()
        params["targetSource"] = str(target)
        url = UMLSWebClient.API_BASE + "crosswalk/{version}/source/{src}/code/{code}".format(version=self.version,
                                                                                             src=source,
                                                                                             code=code,
                                                                                             )
        resp = requests.get(url, params=params)
        resp.raise_for_status()
        return json.loads(resp.text)
