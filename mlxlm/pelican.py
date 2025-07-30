#!/usr/bin/env python

from mlx_lm import load, generate

model, tokenizer = load("mlx-community/Mistral-7B-Instruct-v0.3-4bit")

prompt = "Generate an SVG of a pelican riding a bicycle"

messages = [{"role": "user", "content": prompt}]

prompt = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True
)

text = generate(model, tokenizer, prompt=prompt, verbose=True, max_tokens=2000)


