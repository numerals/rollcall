import unittest
from datetime import date, timedelta
from rollcall.func_json import gen_dict, format_date, TAGS
from rollcall.display import total_classes

class TestTotalClassesHeld(unittest.TestCase):
    """
    tests the total_classes_help function in display module
    """
    def setUp(self):
        self.today = date.today()
        self.json = gen_dict(self.today, [0,1,2,3,4,5,6], 1)

    def test_total_classes_held(self):
        for x in range(len(self.json)):
            current = self.today + timedelta(days=x)
            formatted = format_date(current)
            held = total_classes(self.json, formatted)
            self.assertEqual(len(held), x)
