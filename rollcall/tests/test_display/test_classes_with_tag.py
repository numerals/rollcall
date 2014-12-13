import unittest
from datetime import date, timedelta
from rollcall.func_json import gen_dict, update_status, format_date, TAGS
from rollcall.display import classes_with_tag

class TestClassesWithTag(unittest.TestCase):
    """
    tests the classes_with_tag function in display module
    """
    def setUp(self):
        self.today = date.today()
        self.json = gen_dict(self.today, [0,1,2,3,4,5,6], 1)
        self.length = len(self.json)

    def test_classes_with_tag(self):
        for x in range(self.length):
            current = self.today + timedelta(days=x)
            formatted = format_date(current)
            classes = classes_with_tag(self.json, TAGS['f'])
            self.assertEqual(len(classes), self.length - x)
            update_status(self.json, formatted, TAGS['p'])
