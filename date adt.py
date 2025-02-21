class DateADT:
    def __init__(self, year, month, day):
         self.year = year
         self.month = month
         self.day = day
    def __repr__(self):
         return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"

    def set_date(self, year, month, day):
         self.year = year
         self.month = month
         self.day = day
    def get_date(self):
         return (self.year, self.month, self.day)
    def is_leap_year(self):
         if (self.year % 4 == 0 and self.year % 100 != 0 or self.year % 400 == 0):
             return True
         return False
    def add_days(self, days):
         days_in_month = [31, 29 if self.is_leap_year()else 28,31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
         self.day += days
         while self.day > days_in_month[self.month-1]:
             self.day-= days_in_month[self.month-1]
             self.month += 1
             if self.month > 12:
                 self.month = 1
                 self.year += 1
 # Example usage:
date = DateADT(2024, 6, 29)
print(date)
date.add_days(5)
print(date)
print(date.is_leap_year())

'''class DateADT:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self):
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"

    def set_date(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def get_date(self):
        return (self.year, self.month, self.day)

    def is_leap_year(self):
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            return True
        return False

    def add_days(self, days):
        days_in_month = [31, 29 if self.is_leap_year() else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.day += days
        while self.day > days_in_month[self.month - 1]:
            self.day -= days_in_month[self.month - 1]
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1


# Example usage:
date = DateADT(2024, 6, 29)
print(date)
date.add_days(5)
print(date)
print(date.is_leap_year())
'''
