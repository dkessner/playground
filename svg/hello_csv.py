#!/usr/bin/env python

import csv

#
# File,Number,Model,Min X,Min Y,Max X,Max Y
#   0    1      2     3     4     5     6
#

with open('test.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        id = row[1]
        x1, y1, x2, y2 = row[3:7]
        print(id, x1, y1, x2, y2)

