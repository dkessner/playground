#!/usr/bin/env python

from sentence_transformers import SentenceTransformer, util

base_sentence = "I'm ecstatic"
sentences = ["I'm happy", "I'm full of happiness", "I'm elated",
        "I'm sad", "I'm poor", "The quick brown fox"]

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

print("base sentence:", base_sentence)

embedding_1= model.encode(base_sentence, convert_to_tensor=True)

for sentence in sentences:
    embedding_2 = model.encode(sentence, convert_to_tensor=True)
    print(sentence, util.pytorch_cos_sim(embedding_1, embedding_2))


