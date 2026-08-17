# 导包
import torch
import numpy as np

# 1. 定义函数, 演示: torch.tensor 根据指定数据创建张量
def dm01():
    # 场景1: 标量 张量
    t1 = torch.tensor(1)
    print(f't1：{t1}, t1类型：{type(t1)}')
    print('-' * 50)

    # 场景2: 二维列表 -> 张量.
    data = [[1,2,3],[4,5,6],[7,8,9]]
    t2 = torch.tensor(data)
    print(f't2：{t2}, t2类型：{type(t2)}')
    print('-' * 50)

    # 场景3: numpy nd数组 -> 张量.
    data = np.random.randint(low = 0, high = 10, size = (3,4))
    t3 = torch.tensor(data)
    print(f't3：{t3}, t3类型：{type(t3)}')
    print('-' * 50)

    # 场景4: 尝试直接创建 指定维度(例如: 2行3列的)张量
    # t4 = torch.tensor(2, 3)               # 报错.
    # print(f't4: {t4}, type: {type(t4)}')

    # 2. 定义函数, 演示: torch.Tensor 根据形状创建张量, 其也可用来创建指定数据的张量
def dm02():
    # 场景1: 标量 张量        (这里不是生成标量 张量，而是生成10个元素的向量 张量)
    t1 = torch.Tensor(10)
    print(f't1：{t1}, t1类型：{type(t1)}')
    print('-' * 50)

    # 场景2: 二维列表 -> 张量.
    data = [[1,2,3],[4,5,6],[7,8,9]]
    t2 = torch.Tensor(data)
    print(f't2：{t2}, t2类型：{type(t2)}')
    print('-' * 50)

    # 场景3: numpy nd数组 -> 张量.
    data = np.random.randint(low = 0, high = 10, size = (3,4))
    t3 = torch.Tensor(data)
    print(f't3：{t3}, t3类型：{type(t3)}')
    print('-' * 50)

    # 场景4: 尝试直接创建 指定维度(例如: 2行3列的)张量
    t4 = torch.Tensor(2, 3)
    print(f't4：{t4}, t4类型：{type(t4)}')
    print('-' * 50)

# 3. 定义函数, 演示: torch.IntTensor、torch.FloatTensor、torch.DoubleTensor 创建指定类型的张量
def dm03():
    # 场景1: 标量 张量        (这里不是生成标量 张量，而是生成10个元素的向量 张量)
    t1 = torch.IntTensor(10)
    print(f't1：{t1}, t1类型：{type(t1)}')
    print('-' * 50)

    # 场景2: 二维列表 -> 张量.
    data = [[1,2,3],[4,5,6],[7,8,9]]
    t2 = torch.IntTensor(data)
    print(f't2：{t2}, t2类型：{type(t2)}')
    print('-' * 50)

    # 场景3: numpy nd数组 -> 张量.
    data = np.random.randint(low = 0, high = 10, size = (3,4))
    t3 = torch.IntTensor(data)
    print(f't3：{t3}, t3类型：{type(t3)}')
    print('-' * 50)

    # 场景4: 如果类型不匹配, 会尝试自动转换类型.
    data = np.random.randint(low = 0, high = 10, size = (3,4))
    t4 = torch.FloatTensor(data)
    print(f't4：{t4}, t4类型：{type(t4)}')
    print('-' * 50)
    
    # 场景5: 尝试直接创建 指定维度(例如: 2行3列的)张量
    t5 = torch.IntTensor(2, 3)
    print(f't5：{t5}, t5类型：{type(t5)}')
    print('-' * 50)

if __name__ == '__main__':
    # dm01()
    # dm02()
    dm03()