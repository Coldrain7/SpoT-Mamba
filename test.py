import torch
import sys
print(f"Python版本: {sys.version}")
a = torch.tensor([
    [0, 2, 3, 0, 0, 0],
    [2, 0, 0, 2, 2, 0],
    [3, 0, 0, 2, 0, 0],
    [0, 2, 2, 0, 2, 2],
    [0, 2, 0, 2, 0, 3],
    [0, 0, 0, 2, 3, 0]])
b = a.matmul(a)
print('=' * 100)
print('=' * 100)
print('=' * 50)

