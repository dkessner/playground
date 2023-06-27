#!/usr/bin/env python
#
# csv2svg.py
#

import csv
import drawsvg


# hard-coded for now
imageWidth = 1086
imageHeight = 1086


d = drawsvg.Drawing(imageWidth, imageHeight)

#
# File,Number,Model,Min X,Min Y,Max X,Max Y
#   0    1      2     3     4     5     6
#

with open('test.csv') as csvfile:
    reader = csv.reader(csvfile)
    next(reader) # skip header line
    for row in reader:
        number = row[1]
        x, y, x_end, y_end = row[3:7]
        predict = row[19]
        live = True if predict == "Live" else False

        w = int(x_end)-int(x)
        h = int(y_end)-int(y)
        
        r = drawsvg.Rectangle(x, y, w, h, 
                              stroke='green' if live else 'red', 
                              fill_opacity=0)
        r.append_title(str(number) + " " + predict)
        d.append(r)


d.save_svg('generated.svg')

