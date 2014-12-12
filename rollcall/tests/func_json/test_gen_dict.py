import unittest
import os
from datetime import date, timedelta
from rollcall.tests import helper
from rollcall.func_json import gen_dict, format_date

class Testadd(unittest.TestCase):
    """
    tests the gen_dict function in func_json module
    """
    def test_gen_dict_length(self):
        json = gen_dict(date.today(), [0,1,2,3,4,5,6], 1)
        self.assertEqual(len(json), 7)
        json = gen_dict(date.today(), [0,1,2,3,4,5,6], 16)
        self.assertEqual(len(json), 16 * 7)

    def test_gen_dict_keys(self):
        today = date.today()
        json = gen_dict(today, [0,1,2,3,4,5,6], 1)
        for x in range(len(json)):
            current = today + timedelta(days=x)
            formatted = format_date(current)
            self.assertTrue(json.has_key(formatted))
