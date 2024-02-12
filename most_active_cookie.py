import sys
import csv
from datetime import datetime
from cookie_id_time_pair import CookieIDTimePair

class MostActiveCookie:
    ERROR_MSG_INCORRECT_FILE_DATE_FLAGS = "Incorrect usage. Please use the proper file and date flags (-f and -d)"
    ERROR_MSG_INCORRECT_FILE_FLAG = "Incorrect usage. Please use the proper file flag -f"
    ERROR_MSG_INCORRECT_DATE_FLAG = "Incorrect usage. Please use the proper date flag -d"
    ERROR_MSG_INCORRECT_USAGE = "Incorrect usage. \nPlease follow this format: ./most_active_cookie -f [filename] -d [date]"
    formatter = "%Y-%m-%d"

    def __init__(self):
        self.FILENAME = ""
        self.FILE_FLAG = ""
        self.DATE_FLAG = ""
        self.DATE = ""

    def begin(self, args):

        # check whether the length of args is 5 or not.
        if len(args) != 5:
            print(self.ERROR_MSG_INCORRECT_USAGE)
            return

        self.FILE_FLAG = args[1]
        self.FILENAME = args[2]
        self.DATE_FLAG = args[3]
        self.DATE = args[4]
        # if flags are not valid, then return.
        if not self.are_flags_valid():
            return

        # if date is not valid, then return.
        if not self.is_date_valid():
            return

        try:
            # parse the csv file.
            same_date_cookies_freq = self.parse_csv(self.FILENAME) # parse_csv returns cookie frequency map.
            self.print_most_common_cookie(same_date_cookies_freq) # print the most common cookies.
        except FileNotFoundError:
            print(f"Error: File {self.FILENAME} not found.")
        except Exception as e:
            print(str(e))
    
    def are_flags_valid(self):
        # This method checks whether the file and date flags are correct or not 
        # and displays the error message accordingly if incorrect.
        # It returns True/False according to whether the flags are correct or not.

        if self.FILE_FLAG != "-f" and self.DATE_FLAG != "-d":
            print(self.ERROR_MSG_INCORRECT_FILE_DATE_FLAGS)
            return False

        elif self.FILE_FLAG != "-f":
            print(self.ERROR_MSG_INCORRECT_FILE_FLAG)
            return False

        elif self.DATE_FLAG != "-d":
            print(self.ERROR_MSG_INCORRECT_DATE_FLAG)
            return False

        return True

    def is_date_valid(self):
        # checks whether date is valid and is in correct format or not.

        try:
            datetime.strptime(self.DATE, "%Y-%m-%d")
        except ValueError:
            # Date string is not in the correct format
            print("Error: Date is not in the correct format. Please use the format YYYY-MM-DD.")
            return False

        return True

    def parse_csv(self, filename):
        # This method parses the csv file and also handle edge cases like File Not Found 
        # or Incorrect File Format and raises exception accordingly. 
        # It returns the cookie frequency map.

        parsed_csv = {}

        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # skip header

                for line in reader:
                    # check whether the file is in correct format or not.
                    if len(line) != 2:
                        raise Exception("Error: The file is not in the correct format.")
                    # get the CookieIDTimePair object
                    cookie_id_date_pair_obj = self.parse_cookie_entry(line)
                    # check whether the date is same or not as the specified date.
                    if self.is_same_date(datetime.strptime(self.DATE, self.formatter).date(), cookie_id_date_pair_obj.get_date()):
                        cookie_id = cookie_id_date_pair_obj.get_cookie_id()
                        # update the frequency map.
                        parsed_csv[cookie_id] = parsed_csv.get(cookie_id, 0) + 1

        except FileNotFoundError:
            raise FileNotFoundError(f"Error: File {filename} not found.")

        return parsed_csv

    def is_same_date(self, input_date, target_date):
        return input_date == target_date

    def parse_cookie_entry(self, line):
        # converts line into a CookieIDTimePair object with line[0] as cookieId 
        # and line[1] as date and returns that object.

        cookie_date = datetime.strptime(line[1][:10], self.formatter).date()
        cookie_id_date_pair_obj = CookieIDTimePair(line[0], cookie_date)
        return cookie_id_date_pair_obj

    def print_most_common_cookie(self, same_date_cookies_freq):
        # this method accepts a cookie frequency map and fetches, prints, 
        # and returns the most frequently used cookie(s).

        most_common_cookies = set()
        max_value = 0
        # get the frequency of most frequently used cookie(s)
        for cookie_id, freq in same_date_cookies_freq.items():
            if freq > max_value:
                max_value = freq

        # Fetch the most frequently used cookie(s)
        for cookie_id, freq in same_date_cookies_freq.items():
            if freq == max_value:
                most_common_cookies.add(cookie_id)

        for cookie in most_common_cookies:
            print(cookie)

        return most_common_cookies

if __name__ == "__main__":
    most_active_cookie = MostActiveCookie()
    most_active_cookie.begin(sys.argv)
