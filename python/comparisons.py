#!/usr/bin/env python3
#
# comparisons.py
#

# https://docs.python.org/3/reference/expressions.html#expressions-value-comparisons

a = [1, 2, 3]
b = [1, 2, 3]

print(f"{a==b = }")

c = {'a':1, 'b':2, 'c':3}
d = {'a':1, 'b':2, 'c':3}

print(f"{c==d = }")

d['d'] = 4
print(f"{c==d = }")
d.pop('d')
print(f"{c==d = }")

c['d'] = a
d['d'] = b
print(f"{c==d = }")


