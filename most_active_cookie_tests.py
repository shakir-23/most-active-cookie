import unittest
from datetime import date
from most_active_cookie import MostActiveCookie
from cookie_id_time_pair import CookieIDTimePair

class TestMostActiveCookie(unittest.TestCase):

    def setUp(self):
        self.most_active_cookie = MostActiveCookie()

    def test_is_same_date(self):
        d1 = date(2021, 1, 1)
        d2 = date(2021, 1, 2)
        self.assertFalse(self.most_active_cookie.is_same_date(d1, d2))

    def test_same_date(self):
        d1 = date(2021, 1, 1)
        d2 = date(2021, 1, 1)
        self.assertTrue(self.most_active_cookie.is_same_date(d1, d2))

    def test_parse_token_pair(self):
        values = ["A", "2020-01-01"]
        mock = CookieIDTimePair("A", date(2020, 1, 1))
        self.assertEqual(self.most_active_cookie.parse_cookie_entry(values), mock)
        self.assertIsNotNone(self.most_active_cookie.parse_cookie_entry(values))

    def test_parse_token_pair_false(self):
        values = ["A", "2020-01-02"]
        mock = CookieIDTimePair("A", date(2020, 1, 1))
        self.assertNotEqual(self.most_active_cookie.parse_cookie_entry(values), mock)

    def test_print(self):
        map_data = {"1": 4, "2": 3, "3": 2, "4": 4}
        ret = self.most_active_cookie.print_most_common_cookie(map_data)
        mock = {"4", "1"}
        self.assertSetEqual(ret, mock)

    def test_print_false(self):
        map_data = {"1": 4, "2": 3, "3": 2, "4": 4}
        ret = self.most_active_cookie.print_most_common_cookie(map_data)
        mock = {"4"}
        self.assertNotEqual(ret, mock)
        mock.add("1")
        self.assertSetEqual(ret, mock)

if __name__ == '__main__':
    unittest.main()
