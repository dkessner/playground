#!/usr/bin/env python3
#
# hello_dir.py
#

class A:
    a = 10
    b = 20
    def __init__(self):
        self.c = 5

print("dir():", dir(), sep='\n')
print()

print("dir(A):", dir(A), sep='\n')
print()


