#!/usr/bin/env python
#
# date_range_search.py
#


from datetime import date, timedelta
from random import random


date1 = date(2023, 11, 30)
print(date1)

date2 = date(2024, 3, 7)
print(date2)



def f(d1, d2):
    if random()<.4:
        raise Exception("Failed")
    return [d1.ctime() + " - " + d2.ctime()]


def try_and_retry(f, date_start, date_end):
    try:
        print("trying " + date_start.ctime() + " - " + date_end.ctime())
        return f(date_start, date_end)
    except:
        print("caught failure")
        d = date_end - date_start 

        if d.days < 1:
            message = "End of line: " + date_start.ctime() + " - " + date_end.ctime()
            raise Exception(message)

        midpoint = date_start + d/2

        # return concatenated results
        return try_and_retry(f, date_start, midpoint) + \
               try_and_retry(f, midpoint, date_end)



try:
    result = try_and_retry(f, date1, date2)
    print(result)
except Exception as e:
    print("Caught exception")
    print(e)





