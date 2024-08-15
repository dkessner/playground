#!/usr/bin/env python
#
# nlpbook_ch2_datasets.py
#


from huggingface_hub import list_datasets
from datasets import load_dataset

import pandas as pd
import matplotlib.pyplot as plt


#all_datasets = [*list_datasets()]
#print("len(all_datasets): " , len(all_datasets))

emotions = load_dataset("emotion")
print("emotions:", emotions)

ds_train = emotions['train']
print("len(ds_train):", len(ds_train))

print("ds_train[0]:", ds_train[0])
print("column_names:", ds_train.column_names)
print("features:", ds_train.features)
print()

print("iteration:")
for i in range(5):
    print(i, ds_train[i])
print()

print("first 5 records")
print(ds_train[:5])
print()

print('single column')
print(ds_train['text'][:5])
print()


print('pandas')
emotions.set_format(type='pandas')
df = emotions["train"][:]
print(df.head())
print()

# class features have an int2str method
label_int2str = emotions["train"].features["label"].int2str

df["label_string"] = df["label"].apply(label_int2str)
print(df.head())
print()

# plot class distribution

df["label_string"].value_counts(ascending=True).plot.barh()
plt.title("Frequency of classes")
plt.show()

# plot word count distributions

df["word_count"] = df["text"].str.split().apply(len)
print(df.head())
print()

df.boxplot("word_count", by='label_string', grid=False, showfliers=False, color='black')
plt.suptitle("")
plt.xlabel("")
plt.show()



