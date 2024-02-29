#!/usr/bin/env python
#
# make_house_tiny_csv.py
#


# https://d2l.ai/chapter_preliminaries/pandas.html

 
import os

os.makedirs('data', exist_ok=True)
filename = os.path.join('data', 'house_tiny.csv')
with open(filename, 'w') as f:
    f.write('''NumRooms,RoofType,Price
NA,NA,127500
2,NA,106000
4,Slate,178100
NA,NA,140000''')


