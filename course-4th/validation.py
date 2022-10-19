
import numpy as np
import torch
torch.manual_seed(0)


x = torch.randn(10, 4, requires_grad=True)
W = torch.randn(4, 4, requires_grad=True)
y = torch.randn(10, 4, requires_grad=True)

# f = (torch.clamp(x.mm(W), 0) - y).pow(2).sum()
z = x.mm(W)
y_hat = torch.clamp(z, 0)
f = (y_hat - y).pow(2).sum()

f.backward()
# print('W_grid: ', W.grad)
# print('X_grid: ', x.grad)
# print('Y_grid: ', y.grad)

# validation
J = np.where(z > 0, 1, 0).astype('float32')
J = torch.from_numpy(J)
W_grad = 2*x.t().mm((y_hat - y)*J)
x_grad = (2*(y_hat - y)*J).mm(W.t())
y_grad = -2*(y_hat - y)

print(W.grad == W_grad)
print(x.grad == x_grad)
print(y.grad == y_grad)



















