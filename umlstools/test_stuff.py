import unittest

import UMLSWebClient as wc

class TestUMLSWebClient(unittest.TestCase):
    def setUp(self):
        self.client = wc.UMLSWebClient()

    def test_crosswalk(self):
        print(self.client.crosswalk("E11.3291", "ICD10CM"))

    def test_search(self):
        results = self.client.search("broken", page_number=1)
        for result in results:
            print(result['ui']+" "+result["name"])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUMLSWebClient)
    unittest.TextTestRunner(verbosity=2).run(suite)
