#!/usr/bin/env python
#
# nlpbook_ch5_unicorn.py
#



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


max_length = 128

input_txt = """In a shocking finding, scientist discovered \
a herd of unicorns living in a remote, previously unexplored \
valley, in the Andes Mountains. Even more surprising to the \
researchers was the fact that the unicorns spoke perfect English.\n\n
"""

input_ids = tokenizer(input_txt, return_tensors="pt")["input_ids"].to(device)
output_greedy = model.generate(input_ids, max_length=max_length, 
                               do_sample=False)

## beam search

import torch.nn.functional as F

def log_probs_from_logits(logits, labels):
    logp = F.log_softmax(logits, dim=-1)
    logp_label = torch.gather(logp, 2, labels.unsqueeze(2)).squeeze(-1)
    return logp_label

def sequence_logprob(model, labels, input_len=0):
    with torch.no_grad():
        output = model(labels)
        log_probs = log_probs_from_logits(
            output.logits[:, :-1, :], labels[:, 1:])
        seq_log_prob = torch.sum(log_probs[:, input_len:])
    return seq_log_prob.cpu().numpy()


logp = sequence_logprob(model, output_greedy, input_len=len(input_ids[0]))


print("## greedy")
print(tokenizer.decode(output_greedy[0]))
print(f"\nlog-prob: {logp:.2f}")


output_beam = model.generate(input_ids, max_length=max_length, num_beams=5, 
                             do_sample=False)
logp = sequence_logprob(model, output_beam, input_len=len(input_ids[0]))

print("## beam")
print(tokenizer.decode(output_beam[0]))
print(f"\nlog-prob: {logp:.2f}")



