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

# dir() returns the list of names in the global scope
# globals() returns a dict: name -> function/class

print("globals():", globals(), sep='\n')
print()

print("globals()['A']", globals()['A']) # the actual class A
print()

