from datetime import datetime as dt
from datetime import timezone, timedelta

now = dt.now(timezone.utc)
print(now)
print(type(now))

#STRING TO DATE
date_string = "2025-10-30 18:53:00"
date_object = dt.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(date_object)
print(type(date_object))

#DATE TO STRING
date_string = dt.strftime(date_object, "%y-%m-%d %H:%M:%S")
print(date_string)

#adding 5 days to current time

five_days = timedelta(days=5)
new_date = now + five_days
print(new_date)