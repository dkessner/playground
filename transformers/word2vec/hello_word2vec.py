#!/usr/bin/env python
#
# hello_word2vec.py
#


import gensim
import gensim.downloader
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances


def get_models():
    models = list(gensim.downloader.info()['models'].keys())
    return models

# print("models:", get_models())

# word2vec-google-news-300

model_name = 'word2vec-google-news-300'
print("loading model:", model_name)
model = gensim.downloader.load(model_name)

#model = gensim.models.Word2Vec.load_word2vec_format('path-to-vectors.txt', binary=False)

# if you vector file is in binary format, change to binary=True
#sentence = ["London", "is", "the", "capital", "of", "Great", "Britain"]

sentence = "boy girl man woman".split()
vectors = [model[w] for w in sentence if w in model]


#for word, vector in zip(sentence, vectors):
#    print(word, vector, "\n")


sentence.append("boy-girl")
vectors.append(model["boy"] - model["girl"])

sentence.append("man-woman")
vectors.append(model["man"] - model["woman"])


with open('vectors.txt','w') as f:
    for vector in vectors:
        f.write('\t'.join(str(v) for v in vector) + '\n')
        
with open('metadata.txt','w') as f:
    for word in sentence:
        f.write(word + '\n')



## explore

v_boy = model["boy"]
v_girl = model["girl"]
v_man = model["man"]
v_woman = model["woman"]

test = v_man - v_boy + v_girl
vectors.append(test)

similarities = cosine_similarity(vectors)
distances = euclidean_distances(vectors)

print("similarities:\n", similarities, sep='')
print("distances:\n", distances, sep='')





