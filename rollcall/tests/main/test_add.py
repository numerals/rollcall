import unittest
import os
import helper
from rollcall.main import add, fileExists
from rollcall.exceptions import SubjectExists

class Testadd(unittest.TestCase):
    """
    tests the add function in main module
    """
    def setUp(self):
        self.dire = os.path.dirname(__file__)
        self.json = ''
        self.dummy = os.path.join(self.dire, 'dummy.json')
        self.new = os.path.join(self.dire, 'new.json')
        helper.newFile(self.dummy)

    def test_add_file_exists(self):
        self.assertTrue(fileExists(self.dummy))
        self.assertRaises(SubjectExists, add, self.json, self.dummy)

    def test_add_file_does_not_exist(self):
        self.assertFalse(fileExists(self.new))
        add(self.json, self.new)
        self.assertTrue(fileExists(self.new))
        os.remove(self.new)

    def tearDown(self):
        os.remove(self.dummy)
