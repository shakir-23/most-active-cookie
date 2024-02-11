class CookieIDTimePair:
    def __init__(self, cookieId, date):
        self.cookieId = cookieId
        self.date = date

    def get_cookie_id(self):
        return self.cookieId

    def get_date(self):
        return self.date
    
    def __eq__(self, other):
        if not isinstance(other, type(self)):
            # if the other item of comparison is not of this class
            return NotImplemented

        # return True or False based on if self's attributes match other's
        return self.cookieId == other.cookieId and self.date == other.date