from datetime import date
current=date.today()
print("current time is:",current.day)
print("current month is:",current.month)
print("current year is:",current.year)
print(current.strftime("%d%m%y"))
