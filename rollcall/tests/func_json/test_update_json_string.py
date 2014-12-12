import unittest
import os
from datetime import date, timedelta
from rollcall.exceptions import NoDate
from rollcall.tests import helper
from rollcall.func_json import *

class Testadd(unittest.TestCase):
    """
    tests the update_json_string function in func_json module
    """
    def setUp(self):
        self.today = date.today()
        self.json = gen_dict(date.today(), [0,1,2,3,4,5,6], 1)
        self.length = len(self.json)
        self.str_json = dict_to_json(self.json)

    def test_update_json_string_length(self):
        new_json = update_json_string(self.str_json, self.today, 'check')
        new_json = json_to_dict(new_json)
        self.assertEqual(self.length, len(new_json))

    def test_update_json_string_keys(self):
        str_json = self.str_json
        for x in range(self.length):
            current = self.today + timedelta(days=x)
            str_json = update_json_string(str_json, current, 'check')
        str_json = json_to_dict(str_json)
        for x in range(self.length):
            current = self.today + timedelta(days=x)
            formatted_date = format_date(current)
            self.assertEqual('check', str_json[formatted_date])

    def test_update_json_string_no_such_date(self):
        anything = self.today + timedelta(days=self.length)
        self.assertRaises(NoDate, update_json_string, self.str_json, anything, 'check')


