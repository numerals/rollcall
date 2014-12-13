import unittest
from datetime import date, timedelta
from rollcall.func_json import gen_dict, get_status, format_date
from rollcall.exce import NoField

class Testadd(unittest.TestCase):
    """
    tests the get_status function in func_json module
    """
    def setUp(self):
        self.today = date.today()
        self.json = gen_dict(self.today, [0,1,2,3,4,5,6], 1)
        self.length = len(self.json)

    def test_get_status_field_exists(self):
        for x in range(self.length):
            current = self.today + timedelta(days=x)
            formatted = format_date(current)
            self.assertEqual(get_status(self.json, formatted), 'future')
            self.assertEqual(len(self.json), self.length)

    def test_get_status_field_does_not_exists(self):
        anything = self.today + timedelta(days=self.length)
        self.assertRaises(NoField, get_status, self.json, anything)
