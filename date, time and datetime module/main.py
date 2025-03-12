from datetime import *


now = datetime.now()
print(now)

print("year now:", now.year)
print("month now:", now.month)
print("day now:", now.day)
print("hour now:", now.hour)
print("seconds now:", now.second)
print("microseconds now:", now.microsecond)

print("-" * 10)

# formatting
formatted_date = now.strftime("%d-%B-%y %I:%M:%S %p")

print(formatted_date)


date1 = datetime(2025, 3, 12)
date2 = datetime(2012, 5, 31)

diff = date1 - date2

print(diff)

days = ["mon", "tues", 'wed', 'thurs', 'fri', 'sat', 'sun']

print("Todays weekday is:", days[now.weekday()])