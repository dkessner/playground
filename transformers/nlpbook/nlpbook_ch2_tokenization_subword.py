#!/usr/bin/env python
#
# nlpbook_ch2_tokenization_subword.py
#

# subword tokenization

from transformers import AutoTokenizer, DistilBertTokenizer

model_checkpoint = "distilbert-base-uncased"


# clean_up_tokenization_spaces=False to silence deprecation warning
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint, clean_up_tokenization_spaces=False)
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

