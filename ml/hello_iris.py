#!/usr/bin/env python

import os
import pandas as pd

df = pd.read_csv("iris.data", header=None, encoding='utf-8')
print(df.tail())

