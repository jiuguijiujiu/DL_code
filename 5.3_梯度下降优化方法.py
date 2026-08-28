import torch
import torch.nn as nn
import torch.optim as optim

def dm01():
    w = torch.tensor(data = [1.0], requires_grad = True, dtype = torch.float)
    criterion = ((w**2)/2.0).sum()
    optimizer = optim.SGD(params = [w], lr = 0.01, momentum = 0.9)

    # 第一次
    optimizer.zero_grad()
    criterion.backward()
    optimizer.step()
    print(w, w.grad)

    # 第二次
    criterion = ((w**2)/2.0).sum()
    optimizer.zero_grad()
    criterion.backward()
    optimizer.step()
    print(w, w.grad)

if __name__ == '__main__':
    dm01()