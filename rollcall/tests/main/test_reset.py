import unittest
import os
from rollcall.tests import helper
from rollcall.main import reset, fileExists

class Testadd(unittest.TestCase):
    """
    tests the reset function in main module
    """
    def setUp(self):
        self.dire = os.path.dirname(__file__)

    def test_reset_on_dir_with_json_files(self):
        self.dummy = os.path.join(self.dire, 'dummy.json')
        helper.newFile(self.dummy)
        self.new = os.path.join(self.dire, 'new.json')
        helper.newFile(self.new)
        self.notjson = os.path.join(self.dire, 'new.blah')
        helper.newFile(self.notjson)
        self.assertTrue(fileExists(self.dummy))
        self.assertTrue(fileExists(self.new))
        reset('.json', self.dire)
        self.assertFalse(fileExists(self.dummy))
        self.assertFalse(fileExists(self.new))
