"""
案例:
    演示PyTorch中如何创建 线性 和 随机张量.

涉及到的函数:
    torch.arange() 和 torch.linspace() 创建线性张量
    torch.random.initial_seed() 和 torch.random.manual_seed() 随机种子设置
    torch.rand/randn() 创建随机浮点类型张量
    torch.randint(low, high, size=()) 创建随机整数类型张量

要掌握的函数:
    arange(), linspace(), manual_seed(), randint()
"""

# 导包
import torch

# 1. 定义函数, 演示: 创建线性张量.
def dm01():
    # 场景1: 创建指定范围的 线性张量.
    # 参1: 起始值, 参2: 结束值, 参3: 步长.
    t1 = torch.arange(0, 11, 2)
    print(f't1: {t1}, type: {type(t1)}')
    print('-' * 50)

    # 场景2: 创建指定范围的 线性张量 -> 等差数列.
    # 参1: 起始值, 参2: 结束值, 参3: 元素的个数
    t2 = torch.linspace(0, 10, 5)
    print(f't2: {t2}, type: {type(t2)}')
    print('-' * 50)

# 2. 定义函数, 演示: 创建随机张量.
def dm02():
    # step1: 设置随机种子.
    # torch.initial_seed()    # 默认采用当前系统的时间戳作为随机种子.
    torch.random.manual_seed(0)
    # step2: 创建随机张量.
    # 场景1: 均匀分布的(0, 1) 随机张量
    t1 = torch.rand(size = (2, 3))
    print(f't1: {t1}, type: {type(t1)}')
    print('-' * 50)

    # 场景2: 符合正态分布的随机张量.
    t2 = torch.randn(size = (2, 3))
    print(f't2: {t2}, type: {type(t2)}')
    print('-' * 50)

    # 场景3: 创建随机整数张量.
    t3 = torch.randint(1, 10, size = (2, 3))
    print(f't3: {t3}, type: {type(t3)}')
    print('-' * 50)

if __name__ == '__main__':
    # dm01()
    dm02()