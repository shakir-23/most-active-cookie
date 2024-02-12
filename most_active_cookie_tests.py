import unittest
from datetime import date
from most_active_cookie import MostActiveCookie
from cookie_id_time_pair import CookieIDTimePair

class TestMostActiveCookie(unittest.TestCase):

    def setUp(self):
        self.most_active_cookie = MostActiveCookie()

    def test_correct_file_date_flags(self):
        self.most_active_cookie.FILE_FLAG = "-f"
        self.most_active_cookie.DATE_FLAG = "-d"
        self.assertTrue(self.most_active_cookie.are_flags_valid())

    def test_incorrect_file_flag(self):
        self.most_active_cookie.FILE_FLAG = "-x"
        self.most_active_cookie.DATE_FLAG = "-d"
        self.assertFalse(self.most_active_cookie.are_flags_valid())

    def test_incorrect_date_flag(self):
        self.most_active_cookie.FILE_FLAG = "-f"
        self.most_active_cookie.DATE_FLAG = "-x"
        self.assertFalse(self.most_active_cookie.are_flags_valid())

    def test_incorrect_file_date_flags(self):
        self.most_active_cookie.FILE_FLAG = "-x"
        self.most_active_cookie.DATE_FLAG = "-x"
        self.assertFalse(self.most_active_cookie.are_flags_valid())

    def test_is_same_date_false(self):
        d1 = date(2021, 1, 1)
        d2 = date(2021, 1, 2)
        self.assertFalse(self.most_active_cookie.is_same_date(d1, d2))

    def test_is_same_date_true(self):
        d1 = date(2021, 1, 1)
        d2 = date(2021, 1, 1)
        self.assertTrue(self.most_active_cookie.is_same_date(d1, d2))

    def test_parse_cookie_entry_true(self):
        values = ["A", "2020-01-01"]
        mock = CookieIDTimePair("A", date(2020, 1, 1))
        self.assertEqual(self.most_active_cookie.parse_cookie_entry(values), mock)
        self.assertIsNotNone(self.most_active_cookie.parse_cookie_entry(values))

    def test_parse_cookie_entry_false(self):
        values = ["A", "2020-01-02"]
        mock = CookieIDTimePair("A", date(2020, 1, 1))
        self.assertNotEqual(self.most_active_cookie.parse_cookie_entry(values), mock)

    def test_parse_csv_correct_result(self):
        self.most_active_cookie.FILENAME = "cookie_log.csv"
        self.most_active_cookie.formatter = "%Y-%m-%d"
        self.most_active_cookie.DATE = "2018-12-09"
        expected_result = {"AtY0laUfhglK3lC7": 2, "SAZuXPGUrfbcn5UA": 1, "5UAVanZf6UtGyKVS": 1}  # Sample expected result based on test data
        self.assertEqual(self.most_active_cookie.parse_csv(self.most_active_cookie.FILENAME), expected_result)

    def test_parse_csv_incorrect_result(self):
        self.most_active_cookie.FILENAME = "cookie_log.csv"
        self.most_active_cookie.formatter = "%Y-%m-%d"
        self.most_active_cookie.DATE = "2018-12-09"
        expected_result = {"AtY0laUfhglK3lC7": 1, "SAZuXPGUrfbcn5UA": 2, "5UAVanZf6UtGyKVS": 1}  # Sample expected result based on test data
        self.assertNotEqual(self.most_active_cookie.parse_csv(self.most_active_cookie.FILENAME), expected_result)

    def test_parse_csv_file_not_found(self):
        filename = "nonexistent_file.csv"
        with self.assertRaises(FileNotFoundError):
            self.most_active_cookie.parse_csv(filename)
    
    def test_print_most_common_cookie_true(self):
        map_data = {"A": 4, "B": 3, "C": 2, "D": 4}
        ret = self.most_active_cookie.print_most_common_cookie(map_data)
        mock = {"A", "D"}
        self.assertSetEqual(ret, mock)

    def test_print_most_common_cookie_false(self):
        map_data = {"A": 4, "B": 3, "C": 2, "D": 4}
        ret = self.most_active_cookie.print_most_common_cookie(map_data)
        mock = {"D"}
        self.assertNotEqual(ret, mock)
        mock.add("A")
        self.assertSetEqual(ret, mock)

if __name__ == '__main__':
    unittest.main()
