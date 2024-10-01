#!/usr/bin/env python
#
# hello_word2vec.py
#


import gensim
import gensim.downloader


def get_models():
    models = list(gensim.downloader.info()['models'].keys())
    return models

# print("models:", get_models())

# word2vec-google-news-300

model = gensim.downloader.load('word2vec-google-news-300')

#model = gensim.models.Word2Vec.load_word2vec_format('path-to-vectors.txt', binary=False)

# if you vector file is in binary format, change to binary=True
#sentence = ["London", "is", "the", "capital", "of", "Great", "Britain"]

sentence = "king queen man woman".split()
vectors = [model[w] for w in sentence if w in model]


#for word, vector in zip(sentence, vectors):
#    print(word, vector, "\n")


with open('vectors.txt','w') as f:
    for word in sentence:
        f.write('\t'.join(str(v) for v in model[word]) + '\n')
        
with open('metadata.txt','w') as f:
    for word in sentence:
        f.write(word + '\n')



