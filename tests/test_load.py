""" test_loader.py
"""

import unittest
from sdnloader import load

class TestSdnParser(unittest.TestCase):
    """ Test SdnParser
    """
    @classmethod
    def setUpClass(cls):
        cls.loader = load.sdn(url="./tests/sdn_advanced.xml")

    def test_date_of_issue(self):
        """ testing issue date
        """
        self.assertEqual(self.loader.date_of_issue['date_of_issue'], "2024-02-08")

    def test_individual_list(self):
        """ testing indivisual list
        """
        ind_list = self.loader.individual_list()
        self.assertEqual(len(ind_list), 15627)
    
    def test_organization_list(self):
        """ testing organization list
        """
        org_list = self.loader.organization_list()
        self.assertEqual(len(org_list), 16315)