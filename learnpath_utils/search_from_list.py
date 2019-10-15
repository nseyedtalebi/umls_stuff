
import json

import requests

version = 'current'
uri = "https://uts-ws.nlm.nih.gov"
#auth = UMLSWebClient()


def search(auth, search_string, start_page=1, page_size=25, page_limit=1):
    results = []
    tgt = auth.gettgt()
    content_endpoint = "/rest/search/"+version
    page_number = start_page
    page_size = page_size
    while True:
        ticket = auth.getst(tgt)
        query = {'string':search_string,'ticket':ticket, 'pageNumber':page_number, 'pageSize':page_size}
        r = requests.get(uri+content_endpoint,params=query)
        r.encoding = 'utf-8'
        items  = json.loads(r.text)
        json_data = items["result"]
        results.extend(json_data["results"])
        #print(results)
        page_number += 1
        if json_data["results"][0]["ui"] == "NONE" or page_number>page_limit:
            break
    return results


def get_cui_from_ui(auth, ui):
    content_endpoint = "/rest/content/current/CUI/"+str(ui)
    tgt = auth.gettgt()
    ticket = auth.getst(tgt)
    query = {'ticket':auth.getst(tgt)}
    r = requests.get(uri+content_endpoint,params=query)
    r.encoding = 'utf-8'
    items  = json.loads(r.text)
    return items["result"]


def get_from_uri(auth, uri, query={}):
    tgt = auth.gettgt()
    query['ticket'] = auth.getst(tgt)
    r = requests.get(uri, params=query)
    r.encoding = 'utf-8'
    items = json.loads(r.text)
    return items["result"]


def print_alt_def_list(search_terms, results_per_term=5):
    for term in search_terms:
        print("**** Results for '{}' ****".format(term))
        search_results = search(auth, term, page_size=results_per_term)
        for search_result in search_results:
            try:
                concept_info = get_from_uri(auth, search_result['uri'])
            except KeyError:
                continue
            if concept_info['definitions'] != 'NONE':
                def_obj_list = get_from_uri(auth, 
                                        concept_info['definitions'],
                                        query={'pageNumber':1,'pageSize':5})
                def_list = [def_obj['value'] for def_obj in def_obj_list]
            else:
                def_list = []
            print("Concept Name:{} ({})".format(concept_info['name'], concept_info['ui']))
            #print(f"Defs:{def_list}")
            print("Semantic Types:")
            for semantic_type_obj in concept_info['semanticTypes']:
                print("    Type name:{}".format(semantic_type_obj['name']))
                print("    URI:{}".format(semantic_type_obj['uri']))
            print()


def gen_code_using_first_match(search_terms):
    for term in search_terms:
        search_results = search(auth, term, page_size=1)
        search_result = search_results[0]
        try:
            concept_info = get_from_uri(auth, search_result['uri'])
        except KeyError:
            continue
        print("Body_Site(description='{}', parent=None, umls_id='{}').save()".format(concept_info['name'],
                                                                                     concept_info['ui']))


if __name__ == "__main__":
    with open('term_list.txt','r') as inf:
        search_terms = [line.strip() for line in inf]

    print_alt_def_list(search_terms,1)