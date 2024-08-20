#!/usr/bin/env python
#
# nlpbook_ch2_tokenization_subword.py
#



from transformers import AutoTokenizer, DistilBertTokenizer
from datasets import load_dataset

emotions = load_dataset("emotion")
print("emotions:", emotions)


# subword tokenization

model_checkpoint = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint, \
                                          clean_up_tokenization_spaces=False) # silence deprecation warning

distilbert_tokenizer = DistilBertTokenizer.from_pretrained(model_checkpoint, clean_up_tokenization_spaces=False)

text = "The quick brown fox jumps over the lazy dog."
print("text:", text)

encoded_text = tokenizer(text)
print("encoded_text:", encoded_text)

tokens = tokenizer.convert_ids_to_tokens(encoded_text.input_ids)
print("tokens:", tokens)

print("tokens_to_string:", tokenizer.convert_tokens_to_string(tokens))
print("vocab_size:", tokenizer.vocab_size)
print("model_max_length:", tokenizer.model_max_length)
print("model_input_names:", tokenizer.model_input_names)


# tokenization of whole dataset

def tokenize(batch):
    return tokenizer(batch["text"], padding=True, truncation=True)

print("batch tokenization:", tokenize(emotions["train"][:2]))
print()

emotions_encoded = emotions.map(tokenize, batched=True, batch_size=None)

print("emotions column_names:", emotions["train"].column_names)
print("emotions:\n", emotions["train"][0:2])
print()

print("emotions_encoded column_names:", emotions_encoded["train"].column_names)
print("emotions_encoded:\n", emotions_encoded["train"][0:2])
print()






