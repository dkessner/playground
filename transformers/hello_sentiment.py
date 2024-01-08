#!/usr/bin/env python

from transformers import pipeline

from transformers import logging
logging.set_verbosity_error() # suppress warning message


sentiment_pipeline = pipeline("sentiment-analysis")
data = ["I love you", "I hate you", "My name is Inigo Montoya",
        "You killed my father", "Prepare to die"]

result = sentiment_pipeline(data)

for s, sentiment in zip(data, result):
    print(s, sentiment)

