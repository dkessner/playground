#!/usr/bin/env python
#
# bert_sentiment_analysis.py
#


# article:
# https://wandb.ai/mukilan/BERT_Sentiment_Analysis/reports/An-Introduction-to-BERT-And-How-To-Use-It--VmlldzoyNTIyOTA1


import torch
import pandas as pd
import numpy as np
from transformers import BertTokenizer, BertForSequenceClassification


df = pd.read_csv('imdb_movie_reviews.csv')
df = df.drop('sentiment',axis=1)

print(df.head())
print()


tokenizer = BertTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = BertForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
def sentiment_movie_score(movie_review):
	token = tokenizer.encode(movie_review, return_tensors = 'pt')
	result = model(token)
	return int(torch.argmax(result.logits))+1

df['sentiment'] = df['text'].apply(lambda x: sentiment_movie_score(x[:512]))

print(df.head())
print()


