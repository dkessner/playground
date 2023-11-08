from transformers import pipeline

from transformers import logging
logging.set_verbosity_error() # suppress warning message

# sentiment analysis

classifier = pipeline("sentiment-analysis")

result = classifier("I've been waiting for a HuggingFace course my whole life.")
print(result)

result = classifier(
    ["I've been waiting for a HuggingFace course my whole life.", 
     "I hate this so much!"])
print(result)

# classification

classifier = pipeline("zero-shot-classification")

result = classifier(
    "This is a course about the Transformers library",
    candidate_labels=["education", "politics", "business"],
)

print(result)


# translation

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")
result = translator("Ce cours est produit par Hugging Face.")
print(result)
result = translator("Ceci n'est pas un pipe.")
print(result)

