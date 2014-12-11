import unittest
import os
import helper
from datetime import date
from rollcall.main import add, update, fileExists
from rollcall.func_json import gen_dict, dict_to_json
from rollcall.exceptions import UnknownTag, SubjectError

class Testupdate(unittest.TestCase):
    """
    tests the update function in main module
    """
    def setUp(self):
        self.dire = os.path.dirname(__file__)
        self.dummy = os.path.join(self.dire, 'dummy.json')
        helper.newFile(self.dummy)
        self.dummySub = os.path.join(self.dire, 'dummy')
        self.new = os.path.join(self.dire, 'new.json')
        self.sub = os.path.join(self.dire, 'sub.json')
        json = gen_dict(date.today(), [0, 1, 2, 3, 4, 5, 6])
        json = dict_to_json(json)
        add(str(json), 'sub', self.dire)

    def test_update_file_exists(self):
        self.assertTrue(fileExists(self.sub))
        self.assertTrue(update('f', 'sub', self.dire))

    def test_update_file_does_not_exist(self):
        self.assertFalse(fileExists(self.new))
        self.assertRaises(SubjectError, update, 'f', self.new, self.dire)

    def test_update_unknow_tag(self):
        self.assertRaises(UnknownTag, update, 'blahblah', self.dummySub, self.dire)

    def tearDown(self):
        os.remove(self.dummy)
        os.remove(self.sub)
