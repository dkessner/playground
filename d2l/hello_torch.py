#!/usr/bin/env python
#
# hello_torch.py
#


# https://d2l.ai/chapter_preliminaries/ndarray.html


import torch


x = torch.arange(12, dtype=torch.float32)

print("x:", x)
print("x.numel():", x.numel())
print("x.shape:", x.shape)

print("ones((2, 3, 4)):\n", torch.ones((2, 3, 4)))
print("randn(3,4):\n", torch.randn(3, 4))

A = x.reshape(3,4)
print("A:", A)
print("A[-1]:", A[-1])
print("A[1:3]:", A[1:3])

A[2,:] = 13
print("A:", A)
print("A+A:", A+A)
print("A*A:", A*A)
print("2*A:", 2*A)
print("exp(A):", torch.exp(A))

print("A.sum().item():", A.sum().item())
B = A.numpy()
print("A.numpy():", B)
print("torch.from_numpy(B):", torch.from_numpy(B))


