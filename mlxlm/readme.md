# mlx-lm notes



## Reference

[mlx-lm docs](https://qwen.readthedocs.io/en/latest/run_locally/mlx-lm.html)

[mlx-lm GitHub repo](https://github.com/ml-explore/mlx-lm)

## Links

[Simon Willison Space Invaders](https://simonwillison.net/2025/Jul/29/space-invaders/)

[Get started with MLX for Apple Silicon (video)](https://developer.apple.com/videos/play/wwdc2025/315/)

[Explore large language models on Apple silicon with MLX (video)](https://developer.apple.com/videos/play/wwdc2025/298/)


## Installation notes

```
brew install cmake
brew install pkgconf
brew install sentencepiece
brew install protobuf
```


## use with Aider?

[aider + mlx local (blog post)](https://kconner.com/2025/02/17/running-local-llms-with-mlx.html)

[aider + mlx local (reddit)](https://www.reddit.com/r/LocalLLaMA/comments/1fp00jy/apple_m_aider_mlx_local_server/)

```
brew install pipx (if you dont have it)
pipx install mlx-lm
mlx_lm.server --model mlx-community/Qwen2.5-32B-Instruct-8bit --log-level DEBUG
```


