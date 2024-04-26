#!/usr/bin/env python

from transformers import pipeline
unmasker = pipeline('fill-mask', model='bert-base-uncased')
result = unmasker("Hello I'm a [MASK] model.")
print(result)

for record in result:
    print(record['sequence'], record['score'])

