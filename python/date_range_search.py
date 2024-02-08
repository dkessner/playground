#!/usr/bin/env python3
#
# date_range_search.py
#


from datetime import date, timedelta
from random import random
from collections import namedtuple


date1 = date(2023, 11, 30)
print(date1)

date2 = date(2024, 3, 7)
print(date2)



def f(d1, d2):
    if random()<.4:
        raise Exception("Failed")
    return [d1.ctime() + " - " + d2.ctime()]


def try_and_retry(f, date_begin, date_end):
    try:
        print("trying " + date_begin.ctime() + " - " + date_end.ctime())
        return f(date_begin, date_end)
    except:
        print("caught failure")
        d = date_end - date_begin 

        if d.days < 1:
            message = "End of line: " + date_begin.ctime() + " - " + date_end.ctime()
            raise Exception(message)

        midpoint = date_begin + d/2

        # return concatenated results
        return try_and_retry(f, date_begin, midpoint) + \
               try_and_retry(f, midpoint, date_end)


def try_and_retry_nonrecursive(f, date_begin, date_end):
    DateRange = namedtuple("DateRange", ["begin", "end"])
    ranges = [DateRange(date_begin, date_end)]
    result = []

    while len(ranges) > 0:
        range = ranges.pop()
        try:
            print("trying " + range.begin.ctime() + " - " + range.end.ctime())
            result += f(range.begin, range.end)
        except:
            print("Caught exception in f.")
            d = range.end - range.begin 
            if d.days < 1:
                message = "End of line: " + range.begin.ctime() + " - " + range.end.ctime()
                continue
            midpoint = range.begin + d/2
            ranges += [DateRange(midpoint, range.end),
                       DateRange(range.begin, midpoint)]
    return result


try:
    #result = try_and_retry(f, date1, date2)
    result = try_and_retry_nonrecursive(f, date1, date2)
    print(result)
except Exception as e:
    print("Caught exception")
    print(e)





