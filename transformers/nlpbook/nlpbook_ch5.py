#!/usr/bin/env python
#
# nlpbook_ch5.py
#

## get/download tokenizer and model

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

device = "cuda" if torch.cuda.is_available() else "cpu"
model_name = "gpt2-xl"

print("device:", device)
print("model_name:", model_name)

tokenizer = AutoTokenizer.from_pretrained(model_name, 
                                          clean_up_tokenization_spaces=True)

model = AutoModelForCausalLM.from_pretrained(model_name).to(device)

print("tokenizer:", type(tokenizer))
print("model:", type(model))


## text generation

import pandas as pd

input_txt = "Transformers are the"
input_ids = tokenizer(input_txt, return_tensors="pt")["input_ids"].to(device)
iterations = []
n_steps = 8
choices_per_step = 5


print("input_txt:", input_txt)
print("input_ids:", input_ids)



with torch.no_grad():
    for _ in range(n_steps):
        iteration = dict()
        iteration["Input"] = tokenizer.decode(input_ids[0])
        output = model(input_ids=input_ids)

        # Select logits of the first batch and the last token and apply softmax
        next_token_logits = output.logits[0, -1, :]
        next_token_probs = torch.softmax(next_token_logits, dim=-1)
        sorted_ids = torch.argsort(next_token_probs, dim=-1, descending=True)

        # Store tokens with highest probabilities
        for choice_idx in range(choices_per_step):
            token_id = sorted_ids[choice_idx]
            token_prob = next_token_probs[token_id].cpu().numpy()
            token_choice = (
                f"{tokenizer.decode(token_id)} ({100 * token_prob:.2f}%)"
            )
            iteration[f"Choice {choice_idx+1}"] = token_choice
        # Append predicted next token to input
        input_ids = torch.cat([input_ids, sorted_ids[None, 0, None]], dim=-1)
        iterations.append(iteration)
        
df = pd.DataFrame(iterations)
print(df.head())

df.to_csv("iterations.csv")



