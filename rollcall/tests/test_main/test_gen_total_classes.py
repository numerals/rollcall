import unittest
import os, shutil
from datetime import date, timedelta
from rollcall.tests import helper
from rollcall.func_json import format_date
from rollcall.main import gen_total_classes

class TestGenTotalClasses(unittest.TestCase):
    """
    tests the gen_total_classes function in main module
    """
    def setUp(self):
        self.dire = os.path.dirname(__file__)
        self.testArea = os.path.join(self.dire, '../testArea')
        os.mkdir(self.testArea)
        self.weeks = 1
        helper.gen_testData(self.testArea, self.weeks)
        self.today = date.today()

    def test_gen_total_classes_all(self):
        for filename, total in gen_total_classes(dire=self.testArea):
            self.assertEqual(self.weeks * 7, total)

    def test_gen_total_classes_till_today(self):
        for x in range(self.weeks * 7):
            current = self.today + timedelta(days=x)
            f = format_date(current)
            for filename, total in gen_total_classes(field=f, dire=self.testArea):
                self.assertEqual(x, total)

    def tearDown(self):
        shutil.rmtree(self.testArea)
