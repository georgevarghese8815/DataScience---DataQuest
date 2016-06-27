## 1. The time module ##

import time
current_time = time.time()
print(current_time/31557600)

## 2. Converting timestamps ##

import time
current_time = time.time()
current_struct_time = time.gmtime(current_time)
print(current_struct_time)
print(type(current_struct_time))
current_hour = current_struct_time.tm_hour
print(current_hour)

## 3. UTC ##

import datetime
current_datetime = datetime.datetime.now()
print(type(current_datetime))
current_year = current_datetime.year
current_month = current_datetime.month

## 4. Timedelta ##

import datetime
today = datetime.datetime.now()
diff = datetime.timedelta(days = 1)
tomorrow = today + diff
yesterday = today - diff
print(tomorrow)
print(yesterday)
print(today)

## 5. Formatting dates ##

import datetime
mystery_date_formatted_string = mystery_date.strftime("%I:%M%p on %A %B %d, %Y")
print(mystery_date_formatted_string)
times = datetime.datetime.now()
dtimes = times.strftime("%I:%M%p on %A %B %d, %Y")
print(dtimes)

## 6. Parsing dates ##

import datetime
mystery_date = datetime.datetime.strptime(mystery_date_formatted_string, "%I:%M%p on %A %B %d, %Y")
print(mystery_date)
print(type(mystery_date))
temp_date = datetime.datetime.strptime(mystery_date_formatted_string, "%I:%M%p on %A %B %d, %Y")
print(type(temp_date))

## 8. Reformatting our data ##

import datetime
print(posts[-1][2])
for item in posts:
    a = float(item[2])
    b = datetime.datetime.fromtimestamp(a)
    item[2] = b
print(a)
print(b)

## 9. Counting posts in March ##

march_count = 0
for item in posts:
    if item[2].month == 3:
        march_count += 1

## 10. Counting posts in any month ##

import re
def count_posts_in_month(mnth):
    mnth_count = 0
    for row in posts:
        if row[2].month == mnth:
            mnth_count += 1
    return(mnth_count)

feb_count = count_posts_in_month(2)
aug_count = count_posts_in_month(8)