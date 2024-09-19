#!/usr/bin/env python
#
# nlpbook_ch3_attention.py
#

from transformers import AutoTokenizer
from bertviz.transformers_neuron_view import BertModel
from bertviz.neuron_view import show


model_checkpoint = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
model = BertModel.from_pretrained(model_checkpoint)

text = "time flies like an arrow"

show(model, "bert", tokenizer, text, display_mode="light", layer=0, head=8)

