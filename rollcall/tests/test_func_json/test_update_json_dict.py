import unittest
from datetime import date, timedelta
from rollcall.exce import NoField
from rollcall.tests import helper
from rollcall.func_json import *

class Testadd(unittest.TestCase):
    """
    tests the update_json_dict function in func_json module
    """
    def setUp(self):
        self.today = date.today()
        self.json = gen_dict(date.today(), [0,1,2,3,4,5,6], 1)
        self.length = len(self.json)

    def test_update_json_dict_length(self):
        new_json = update_json_dict(self.json, self.today, 'check')
        self.assertEqual(self.length, len(new_json))

    def test_update_json_dict_keys(self):
        json = self.json
        for x in range(self.length):
            current = self.today + timedelta(days=x)
            str_json = update_json_dict(json, current, 'check')
        for x in range(self.length):
            current = self.today + timedelta(days=x)
            formatted_date = format_date(current)
            self.assertEqual('check', json[formatted_date])

    def test_update_json_dict_no_such_date(self):
        anything = self.today + timedelta(days=self.length)
        self.assertRaises(NoField, update_json_dict, self.json, anything, 'check')


