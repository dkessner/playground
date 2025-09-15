#!/usr/bin/env python3
#
# collatz.py
#


import random

value = random.randint(1, 100000)


for i in range(500):
    if i==0 or i>496:
        print(value)
    if value%2 == 0:
        value /= 2
    else:
        value = 3*value+1 



