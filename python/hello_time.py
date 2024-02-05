#!/usr/bin/env python
#
# hello_time.py
#

# Python time library
# https://docs.python.org/3/library/time.html
#
# The epoch is the point where the time starts, the return value of
# time.gmtime(0). It is January 1, 1970, 00:00:00 (UTC) on all platforms.


import time


# seconds since the epoch
t = time.time()
print(t)

# convert to time structure
t_struct = time.localtime(t)
#t_struct = time.gmtime(t)

print("t_struct:", t_struct)

print("year:", t_struct.tm_year)
print("month:", t_struct.tm_mon)
print("day:", t_struct.tm_mday)
print("hour:", t_struct.tm_hour)
print("minute:", t_struct.tm_min)
print("second:", t_struct.tm_sec)


