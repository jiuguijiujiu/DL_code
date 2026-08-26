import torch
import torch.nn as nn

y_ture = torch.tensor([2.0, 2.0, 2.0], dtype = torch.float)

y_pred = torch.tensor([1.0, 1.0, 1.9], dtype = torch.float, requires_grad = True)

criterion = nn.L1Loss()
loss = criterion(y_pred, y_ture)
print(loss)
