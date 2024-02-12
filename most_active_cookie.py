import sys
import csv
from datetime import datetime
from cookie_id_time_pair import CookieIDTimePair

class MostActiveCookie:
    ERROR_MSG_INCORRECT_FLAG = "Incorrect usage. Please use the proper flag (-d)."
    ERROR_MSG_INCORRECT_USAGE = "Incorrect usage. \nPlease follow this format: ./most_active_cookie [filename] [-d] [date]"
    formatter = "%Y-%m-%d"

    def __init__(self):
        self.FILENAME = ""
        self.FILE_FLAG = ""
        self.DATE_FLAG = ""
        self.DATE = ""

    def begin(self, args):
        if len(args) != 5:
            print(self.ERROR_MSG_INCORRECT_USAGE)
            return

        self.FILE_FLAG = args[1]
        self.FILENAME = args[2]
        self.DATE_FLAG = args[3]
        self.DATE = args[4]

        if self.DATE_FLAG != "-d" or self.FILE_FLAG != "-f":
            print(self.ERROR_MSG_INCORRECT_FLAG)
            return

        try:
            same_date_cookies_freq = self.parse_csv(self.FILENAME)
            self.print_most_common_cookie(same_date_cookies_freq)
        except FileNotFoundError:
            print(f"Error: File {self.FILENAME} not found.")
        except Exception as e:
            print(str(e))

    def parse_csv(self, filename):
        parsed_csv = {}

        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # skip header

                for line in reader:
                    if len(line) != 2:
                        raise Exception("Error: The file is not in the correct format.")

                    cookie_id_date_pair_obj = self.parse_cookie_entry(line)

                    if self.is_same_date(datetime.strptime(self.DATE, self.formatter).date(), cookie_id_date_pair_obj.get_date()):
                        cookie_id = cookie_id_date_pair_obj.get_cookie_id()
                        parsed_csv[cookie_id] = parsed_csv.get(cookie_id, 0) + 1

        except FileNotFoundError:
            raise FileNotFoundError(f"Error: File {filename} not found.")

        return parsed_csv

    def is_same_date(self, input_date, target_date):
        return input_date == target_date

    def parse_cookie_entry(self, line):
        cookie_date = datetime.strptime(line[1][:10], self.formatter).date()
        cookie_id_date_pair_obj = CookieIDTimePair(line[0], cookie_date)
        return cookie_id_date_pair_obj

    def print_most_common_cookie(self, same_date_cookies_freq):
        to_print = set()
        max_value = 0

        for key, value in same_date_cookies_freq.items():
            if value == max_value:
                to_print.add(key)
            elif value > max_value:
                to_print.clear()
                max_value = value
                to_print.add(key)

        for cookie in to_print:
            print(cookie)

        return to_print

if __name__ == "__main__":
    most_active_cookie = MostActiveCookie()
    most_active_cookie.begin(sys.argv)
