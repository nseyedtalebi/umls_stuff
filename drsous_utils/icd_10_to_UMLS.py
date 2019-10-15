from itertools import chain

from umlstools.UMLSWebClient import UMLSWebClient

'''
This is buggy - it fails on input "H40.021" by leaving off the leading zero: "H40.22"
is the output, but it should be "H40.022". Note that the former is a completely
different code from the latter!
'''
def add_one(icd_code):
    parts = icd_code.split(".")
    parts[1] = str(int(parts[1])+1)
    return ".".join(parts)

c = UMLSWebClient()
all_codes = (
    "E11.3291",
    "E11.3211",
    "E11.3391",
    "E11.3491",
    "E11.3411",
    "E11.3591",
    "E11.3511",
    "H35.3110",
    "H40.021",
    "E11.3292",
    "E11.3212",
    "E11.3392",
    "E11.3492",
    "E11.3412",
    "E11.3592",
    "E11.3512",
    "H35.3111",
    "H40.022",
    "E11.9",
)

for icd in all_codes:
    res = c.search(icd, input_type="code", search_type="exact", sabs=["ICD10CM"])
    for umls in res:
        print('Diagnosis.objects.update_or_create(umls_id="{}", icd10_code="{}", description="{}")'.format(umls["ui"], icd, umls["name"]))
