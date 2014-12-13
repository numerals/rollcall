import unittest
import os
from datetime import date
from rollcall.main import add, get_json_file, fileExists
from rollcall.func_json import gen_dict, dict_to_json
from rollcall.exce import SubjectError

class Testupdate_json_file(unittest.TestCase):
    """
    tests the get_json_file function in main module
    """
    def setUp(self):
        self.dire = os.path.dirname(__file__)
        self.new = os.path.join(self.dire, 'new.json')
        self.sub = os.path.join(self.dire, 'sub.json')
        self.json = gen_dict(date.today(), [0, 1, 2, 3, 4, 5, 6])
        json_str = dict_to_json(self.json)
        add(str(json_str), self.sub)

    def test_get_json_file_exists(self):
        self.assertTrue(fileExists(self.sub))
        json = get_json_file(self.sub)
        self.assertEqual(self.json, json)

    def test_update_json_file_file_does_not_exist(self):
        self.assertFalse(fileExists(self.new))
        self.assertRaises(SubjectError, get_json_file, self.new)

    def tearDown(self):
        os.remove(self.sub)

