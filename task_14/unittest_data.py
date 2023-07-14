import unittest
from data import final_check_year
class TestPrime(unittest.TestCase):
    def test_leap_year(self):
        self.assertEqual(final_check_year("12.12.2000"), 'Високосный')

    def test_not_leap_year(self):
        self.assertEqual(final_check_year("12.12.1993"), 'не является високосным')

    def test_year_is_int(self):
        self.assertEqual(final_check_year(123), 'Дата заполнена не корректно')

    def test_year_is_other_str(self):
        self.assertEqual(final_check_year("adadsda"), 'Дата заполнена не корректно')

    def test_year_bottom_line(self):
        self.assertEqual(final_check_year("12.12.0000"), 'Дата заполнена не корректно')

    def test_year_top_line(self):
        self.assertEqual(final_check_year("12.12.10000"), 'Дата заполнена не корректно')


if __name__ == '__main__':
    unittest.main(verbosity=True)