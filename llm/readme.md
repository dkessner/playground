# Notes on LLM CLI tool

[LLM CLI tool](https://llm.datasette.io/en/stable/)


[https://simonwillison.net/2025/Feb/15/llm-mlx/](https://simonwillison.net/2025/Feb/15/llm-mlx/)


## Installation


Install `llm`
```
pip install llm
```

Install `llm-mlx` plugin
```
llm install llm-mlx
```

Download and register a model.
```
llm mlx download-model mlx-community/Llama-3.2-3B-Instruct-4bit
```

Run prompts.
```
llm -m mlx-community/Llama-3.2-3B-Instruct-4bit 'Python code to traverse a tree, briefly'
```

Set and use aliases for models.
```
llm aliases set l32 mlx-community/Llama-3.2-3B-Instruct-4bit
llm -m l32 'a joke about a haggis buying a car'
```


## Explore aider


Qwen
```
llm mlx download-model mlx-community/Qwen2.5-0.5B-Instruct-4bit
llm -m mlx-community/Qwen2.5-0.5B-Instruct-4bit 'Python code to traverse a tree, briefly'
```

Run server + aider
```
mlx_lm.server --model mlx-community/Qwen2.5-0.5B-Instruct-4bit --log-level DEBUG
aider --openai-api-base http://localhost:8080/v1/ --openai-api-key secret --model openai/mlx-community/Qwen2.5-0.5B-Instruct-4bit
```


## Explore llm tool 

Large download
```
llm mlx download-model mlx-community/gemma-3-27b-it-8bit
```

```
llm -m mlx-community/gemma-3-27b-it-8bit 'describe this image' -a https://static.simonwillison.net/static/2024/pelicans.jpg
```



## Not tried


```
llm mlx download-model Qwen/Qwen3-Coder-480B-A35B-Instruct
llm mlx download-model Qwen/Qwen3-Coder-30B-A3B-Instruct
```
```
llm mlx download-model mlx-community/Qwen3-Coder-30B-A3B-Instruct-4bit-dwq-v2
llm mlx download-model mlx-community/Mistral-Small-24B-Instruct-2501-4bit
```

