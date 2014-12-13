import unittest
import os, shutil
from rollcall.tests import helper
from rollcall.main import gen_classes_with_tag

class TestGenClassesWithTag(unittest.TestCase):
    """
    tests the gen_classes_with_tag function in main module
    """
    def setUp(self):
        self.dire = os.path.dirname(__file__)
        self.testArea = os.path.join(self.dire, '../testArea')
        os.mkdir(self.testArea)
        self.weeks = 1
        self.length = self.weeks * 7
        helper.gen_testData(self.testArea, self.weeks)

    def test_gen_classes_with_tag(self):
        for filename, total in gen_classes_with_tag(dire=self.testArea):
            name, extension = os.path.splitext(filename)
            expected = int(name)
            self.assertEqual(expected, total)

    def tearDown(self):
        shutil.rmtree(self.testArea)


