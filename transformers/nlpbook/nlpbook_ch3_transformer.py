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

## feed-forward layer

class FeedForward(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.linear_1 = nn.Linear(config.hidden_size, config.intermediate_size)
        self.linear_2 = nn.Linear(config.intermediate_size, config.hidden_size)
        self.gelu = nn.GELU()
        self.dropout = nn.Dropout(config.hidden_dropout_prob)

    def forward(self, x):
        x = self.linear_1(x)
        x = self.gelu(x)
        x = self.linear_2(x)
        x = self.dropout(x)
        return x

feed_forward = FeedForward(config)
ff_outputs = feed_forward(attn_outputs)
print("ff_outputs.size():", ff_outputs.size())


## layer normalization

class TransformerEncoderLayer(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.layer_norm_1 = nn.LayerNorm(config.hidden_size)
        self.layer_norm_2 = nn.LayerNorm(config.hidden_size)
        self.attention = MultiHeadAttention(config)
        self.feed_forward = FeedForward(config)

    def forward(self, x):
        x = x + self.attention(self.layer_norm_1(x)) # attention + skip connection
        x = x + self.feed_forward(self.layer_norm_2(x)) # feed forward + skip connection
        return x


encoder_layer = TransformerEncoderLayer(config)
encoded = encoder_layer(inputs_embeds)
print("encoded.size():", encoded.size())


## positional embeddings

class Embeddings(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.token_embeddings = nn.Embedding(config.vocab_size,
                                             config.hidden_size)
        self.position_embeddings = nn.Embedding(config.max_position_embeddings,
                                                config.hidden_size)
        self.layer_norm = nn.LayerNorm(config.hidden_size, eps=1e-12)
        self.dropout = nn.Dropout()

    def forward(self, input_ids):
        seq_length = input_ids.size(1)
        position_ids = torch.arange(seq_length, dtype=torch.long).unsqueeze(0)
        token_embeddings = self.token_embeddings(input_ids)
        position_embeddings = self.position_embeddings(position_ids)
        embeddings = token_embeddings + position_embeddings
        embeddings = self.layer_norm(embeddings)
        embeddings = self.dropout(embeddings)
        return embeddings

embedding_layer = Embeddings(config)
print("embedding_layer output size:", embedding_layer(inputs.input_ids).size())


## transformer encoder

class TransformerEncoder(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.embeddings = Embeddings(config)
        self.layers = nn.ModuleList([TransformerEncoderLayer(config) 
                                     for _ in range(config.num_hidden_layers)])
    def forward(self, x):
        x = self.embeddings(x)
        for layer in self.layers:
            x = layer(x)
        return x


encoder = TransformerEncoder(config)
encoded = encoder(inputs.input_ids)
print("encoded.size():", encoded.size())


## classification head

class TransformerForSequenceClassification(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.encoder = TransformerEncoder(config)
        self.dropout = nn.Dropout(config.hidden_dropout_prob)
        self.classifier = nn.Linear(config.hidden_size, config.num_labels)

    def forward(self, x):
        x = self.encoder(x)[:, 0, :]
        x = self.dropout(x)
        x = self.classifier(x)
        return x
        
       
config.num_labels = 3
encoder_classifier = TransformerForSequenceClassification(config)
encoded = encoder_classifier(inputs.input_ids)
print("encoded.size():", encoded.size())



