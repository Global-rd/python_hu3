
from datetime import datetime as dt
from datetime import timezone, timedelta

now = dt.now(timezone.utc)                  # now = dt.now()
print(now)                       # 2025-11-05 18:27:44.017183+00:00
print(type(now))                 # <class 'datetime.datetime'>

# string to date

date_string = "2025-10-25 14:25:14"
date_object = dt.strptime(date_string, "%Y-%m-%d %H:%M:%S")    # https://www.geeksforgeeks.org/python/python-datetime-strptime-function/
print(date_object)
print(type(date_object))           # <class 'datetime.datetime'> date object-é vált

# date to string

date_string = dt.strftime(date_object, "%y*%m*%d %H:%M:%S")
print(date_string)

# adding 5 days to current time

five_days = timedelta(days=5)       # five_days = 5 napnyi idő mennyisége
new_date = now + five_days           # 5 nappal később ugyanabban az időben
print(new_date)




