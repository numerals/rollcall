import unittest
import os, shutil
from rollcall.tests import helper
from rollcall.main import gen_percent

class TestGenPercent(unittest.TestCase):
    """
    tests the gen_percent function in main module
    """
    def setUp(self):
        self.dire = os.path.dirname(__file__)
        self.testArea = os.path.join(self.dire, '../testArea')
        os.mkdir(self.testArea)
        self.weeks = 1
        self.length = self.weeks * 7
        helper.gen_testData(self.testArea, self.weeks)

    def test_gen_percent(self):
        for filename, percent in gen_percent(dire=self.testArea):
            name, extension = os.path.splitext(filename)
            expected = (float(name) / self.length) * 100
            self.assertEqual(expected, percent)

    def tearDown(self):
        shutil.rmtree(self.testArea)

