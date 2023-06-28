#!/usr/bin/env python
#
# csv2svg.py
#

import pandas as pd
import drawsvg


# hard-coded for now
imageWidth = 1086
imageHeight = 1086


d = drawsvg.Drawing(imageWidth, imageHeight)

#
# File,Number,Model,Min X,Min Y,Max X,Max Y
#   0    1      2     3     4     5     6
#

df = pd.read_csv("test.csv")

for index, row in df.iterrows():
    number = row["Number"]
    x, y, x_end, y_end = row[["Min X", "Min Y", "Max X", "Max Y"]]
    predict = row["Predict"]
    live = True if predict == "Live" else False

    w = x_end-x
    h = y_end-y
    
    r = drawsvg.Rectangle(x, y, w, h, 
                          stroke = 'green' if live else 'red', 
                          stroke_width = 3,
                          fill_opacity = 0)
    r.append_title(str(number) + " " + predict)
    d.append(r)


d.save_svg('generated_pandas.svg')

