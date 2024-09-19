#!/usr/bin/env python
#
# nlpbook_ch3_transfomer.py
#


## setup, tokenization

from transformers import AutoTokenizer
from bertviz.transformers_neuron_view import BertModel
from bertviz.neuron_view import show

model_checkpoint = "bert-base-uncased"

tokenizer = AutoTokenizer.from_pretrained(model_checkpoint, 
    clean_up_tokenization_spaces=True) # avoid deprecation warning

model = BertModel.from_pretrained(model_checkpoint)

text = "time flies like an arrow"

inputs = tokenizer(text, return_tensors="pt", add_special_tokens=False)
print("input_ids:", inputs.input_ids)


## embedding

from torch import nn
from transformers import AutoConfig

config = AutoConfig.from_pretrained(model_checkpoint)
token_emb = nn.Embedding(config.vocab_size, config.hidden_size)
print("token_emb:", token_emb)

inputs_embeds = token_emb(inputs.input_ids)
print("input_embeds.size(): [batch_size, seq_len, hidden_dim] == ", inputs_embeds.size())


## query, key, value

import torch
from math import sqrt

query = key = value = inputs_embeds
dim_k = key.size(-1)
scores = torch.bmm(query, key.transpose(1,2)) / sqrt(dim_k)
print(scores.size())


## softmax

import torch.nn.functional as F

weights = F.softmax(scores, dim=-1)
print("weights.sum:", weights.sum(dim=-1))

attn_outputs = torch.bmm(weights, value)
#print("attn_outputs:", attn_outputs)
print("attn_outputs.shape:", attn_outputs.shape)


## attention function

def scaled_dot_product_attention(query, key, value):
    dim_k = query.size(-1)
    scores = torch.bmm(query, key.transpose(1,2)) / sqrt(dim_k)
    weights = F.softmax(scores, dim=-1)
    return torch.bmm(weights, value)

result = scaled_dot_product_attention(query, key, value)
#print("result:", result)
print("result.shape:", result.shape)


## multi-head attention


class AttentionHead(nn.Module):

    def __init__(self, embed_dim, head_dim):
        super().__init__()
        self.q = nn.Linear(embed_dim, head_dim)
        self.k = nn.Linear(embed_dim, head_dim)
        self.v = nn.Linear(embed_dim, head_dim)

    def forward(self, hidden_state):
        attn_outputs = scaled_dot_product_attention(self.q(hidden_state),
                                                    self.k(hidden_state),
                                                    self.v(hidden_state))
        return attn_outputs



class MultiHeadAttention(nn.Module):
    def __init__(self, config):
        super().__init__()
        embed_dim = config.hidden_size
        num_heads = config.num_attention_heads
        head_dim = embed_dim // num_heads
        self.heads = nn.ModuleList(
                [AttentionHead(embed_dim, head_dim) for _ in range(num_heads)]
                )
        self.output_linear = nn.Linear(embed_dim, embed_dim)

    def forward(self, hidden_state):
        x = torch.cat([h(hidden_state) for h in self.heads], dim=-1)
        x = self.output_linear(x)
        return x


multihead_attn = MultiHeadAttention(config)
attn_output = multihead_attn.forward(inputs_embeds)
print("attn_output.size:", attn_output.size())








