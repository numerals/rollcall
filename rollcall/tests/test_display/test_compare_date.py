import unittest
from rollcall.display import compare_date

class TestCompareDate(unittest.TestCase):
    """
    tests the compare_date function in display module
    """
    def test_compare_date_greater(self):
        self.assertEqual(compare_date('1/1/2', '1/1/1'), 1)
        self.assertEqual(compare_date('1/2/2', '1/1/2'), 1)
        self.assertEqual(compare_date('2/2/2', '1/2/2'), 1)

    def test_compare_date_equal(self):
        self.assertEqual(compare_date('1/1/1', '1/1/1'), 0)
        self.assertEqual(compare_date('2/2/2', '2/2/2'), 0)

    def test_compare_date_smaller(self):
        self.assertEqual(compare_date('1/1/1', '1/1/2'), -1)
        self.assertEqual(compare_date('1/1/2', '1/2/2'), -1)
        self.assertEqual(compare_date('1/2/2', '2/2/2'), -1)
