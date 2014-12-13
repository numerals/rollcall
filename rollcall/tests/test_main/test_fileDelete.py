import unittest
import os
from rollcall.tests import helper
from rollcall.main import fileDelete, fileExists

class TestfileDelete(unittest.TestCase):
    """
    tests the fileDelete function in main module
    """
    def setUp(self):
        self.dire = os.path.dirname(__file__)

    def test_fileDelete_file_exists(self):
        self.dummy = os.path.join(self.dire, 'dummy.json')
        helper.newFile(self.dummy)
        self.assertTrue(fileExists(self.dummy))
        self.assertTrue(fileDelete(self.dummy))
        self.assertFalse(fileExists(self.dummy))

    def test_fileDelete_file_does_not_exist(self):
        self.new = os.path.join(self.dire, 'new.json')
        self.assertFalse(fileExists(self.new))
        self.assertFalse(fileDelete(self.new))
        self.assertFalse(fileExists(self.new))
