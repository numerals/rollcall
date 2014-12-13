import unittest
import os
from rollcall.tests import helper
from datetime import date
from rollcall.main import add, update_json_file, fileExists
from rollcall.func_json import gen_dict, dict_to_json
from rollcall.exce import UnknownTag, SubjectError

class Testupdate_json_file(unittest.TestCase):
    """
    tests the update_json_file function in main module
    """
    def setUp(self):
        self.dire = os.path.dirname(__file__)
        self.dummy = os.path.join(self.dire, 'dummy.json')
        helper.newFile(self.dummy)
        self.new = os.path.join(self.dire, 'new.json')
        self.sub = os.path.join(self.dire, 'sub.json')
        json = gen_dict(date.today(), [0, 1, 2, 3, 4, 5, 6])
        json = dict_to_json(json)
        add(str(json), self.sub)

    def test_update_json_file_file_exists(self):
        self.assertTrue(fileExists(self.sub))
        self.assertTrue(update_json_file('f', self.sub))

    def test_update_json_file_file_does_not_exist(self):
        self.assertFalse(fileExists(self.new))
        self.assertRaises(SubjectError, update_json_file, 'f', self.new)

    def test_update_json_file_unknow_tag(self):
        self.assertRaises(UnknownTag, update_json_file, 'blahblah', self.dummy)

    def tearDown(self):
        os.remove(self.dummy)
        os.remove(self.sub)
