# Most Active Cookie
## Tech stack used
This project uses Python3.x and unittest along with a bash script to meet the requirements.

## How to run
The test cases can be executed with the following command:

```./most_active_cookie_tests_script```

The program itself can be executed with the following command:

```./most_active_cookie_script -f [filename] -d [date]```

## Methods used and their usage
- begin()-> This is just the main/entry method of the class.
- parse_csv(filename)-> This method just parses the csv file and returns the cookie frequency mapping.
- are_flags_valid()-> This method checks whether the flags are valid or not.
- is_date_valid()-> Checks whether the date provided is valid and is in the correct format (yyyy-mm-dd) or not.
- is_same_date(input_date, target_date)-> Checks whether the two dates provided are same or not.
- parse_cookie_entry(line)-> Returns CookieIDTimePair objects with line[0] as cookieId and line[1] as date.
- print_most_common_cookie(same_date_cookies_freq)-> Accepts cookie frequency map and prints and returns the most commonly used cookies.