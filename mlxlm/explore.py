#!/usr/bin/env python

from mlx_lm import load, generate
#model, tokenizer = load("mlx-community/GLM-4.5-Air-3bit")
model, tokenizer = load("mlx-community/Qwen3-Coder-480B-A35B-Instruct-4bit")

prompt = "Write an HTML and JavaScript page implementing space invaders"
messages = [{"role": "user", "content": prompt}]
prompt = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True
)

response = generate(
    model, tokenizer,
    prompt=prompt,
    verbose=True,
    max_tokens=8192
)


print(response)

