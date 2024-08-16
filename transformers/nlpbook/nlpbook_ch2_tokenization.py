#!/usr/bin/env python
#
# nlpbook_ch2_tokenization.py
#


import torch
import torch.nn.functional as F


# character-level tokenization

text = "The quick brown fox jumps over the lazy dog."
tokenized_text = list(text)
print("tokenized_text:")
print(tokenized_text)

token2idx = {ch:idx for idx, ch in enumerate(sorted({*tokenized_text}))}
print("token2idx:")
print(token2idx)

tokenized_text_translated = [token2idx[token] for token in tokenized_text]
print("tokenized_text_translated:")
print(tokenized_text_translated)


# one-hot vector encoding

text_tensor = torch.tensor(tokenized_text_translated)
print("text_tensor:")
print(text_tensor)

one_hot_encodings = F.one_hot(text_tensor, num_classes=len(token2idx))
print("one_hot_encodings.shape:")
print(one_hot_encodings.shape) 
print("one_hot_encodings[0]:")
print(one_hot_encodings[0]) 
print("one_hot_encodings[1]:")
print(one_hot_encodings[1]) 


