#!/usr/bin/env python
#
# preprocess_data.py
#


import os
import pandas as pd
import torch


#
# read data 
#

filename = os.path.join('data', 'house_tiny.csv')
data = pd.read_csv(filename)
print("data:\n", data)

#
# clean data
#

inputs, targets = data.iloc[:, 0:2], data.iloc[:, 2]

# replace categorical variable with dummy (boolean indicator) variables
# (and treat NaN as a category)
inputs = pd.get_dummies(inputs, dummy_na=True)

# replace numeric NaN values with mean
inputs = inputs.fillna(inputs.mean())

print("inputs:\n", inputs)

#
# convert to tensors
#


X = torch.tensor(inputs.to_numpy(dtype=float))
y = torch.tensor(targets.to_numpy(dtype=float))
print("X:\n", X)
print("y:\n", y)


