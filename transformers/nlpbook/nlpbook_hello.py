#!/usr/bin/env python
#
# nlpbook_hello.py
#
#

from transformers import pipeline


text = """Dear Amazon, last week I ordered an Optimus Prime action figure \
from your online store in Germany. Unfortunately, when I opened the package, \
I discovered to my horror that I had been sent an action figure of Megatron \
instead! As a lifelong enemy of the Decepticons, I hope you can understand my \
dilemma. To resolve the issue, I demand an exchange of Megatron for the \
Optimus Prime figure I ordered. Enclosed are copies of my records concerning \
this purchase. I expect to hear from you soon. Sincerely, Bumblebee."""


# text classification 
# (defaults to sentiment analysis)

print("text-classification")
classifier = pipeline("text-classification")

outputs = classifier(text)
print(outputs)


# named entity recognition (NER)

print("ner")
ner_tagger = pipeline("ner", aggregation_strategy="simple")
outputs = ner_tagger(text)
print(outputs)

# question answering

reader = pipeline("question-answering")
question = "What does the customer want?"
outputs = reader(question=question, context=text)
print(outputs)

# summarization

summarizer = pipeline("summarization")
outputs = summarizer(text, max_length=45, clean_up_tokenization_spaces=True)
print(outputs)
print("summary_text:", outputs[0]['summary_text'])

# translation

translator = pipeline("translation_en_to_de",
                      model="Helsinki-NLP/opus-mt-en-de")
outputs = translator(text, clean_up_tokenization_spaces=True, min_length=100)
print(outputs)
print("translation_text:", outputs[0]['translation_text'])

# text generation

from transformers import set_seed
set_seed(42) # Set the seed to get reproducible results

generator = pipeline("text-generation")
response = "Dear Bumblebee, I am sorry to hear that your order was mixed up."
prompt = text + "\n\nCustomer service response:\n" + response
outputs = generator(prompt, max_length=200)
print(outputs)
print("generated_text:", outputs[0]['generated_text'])


# BERT example from HF model card

unmasker = pipeline('fill-mask', model='bert-base-uncased')

masked1 = "Hello I'm a [MASK] model."
result = unmasker(masked1)
print(masked1, result)

masked2 = "My name is [MASK].  You killed my father.  Prepare to die."
result = unmasker(masked2)
print(masked2, result)


