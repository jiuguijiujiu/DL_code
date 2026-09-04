import torch
import torchvision
import torchaudio
print('torch:', torch.__version__)
print('torchvision:', torchvision.__version__)
print('torchaudio:', torchaudio.__version__)
print('CUDA:', torch.cuda.is_available())
# 测试创建GPU张量
try:
    a = torch.tensor([1.0]).cuda()
    print('GPU tensor: OK')
except Exception as e:
    print('GPU tensor FAIL:', e)
# 测试torchvision基本操作（resize）
try:
    import torchvision.transforms as T
    T.Resize((224, 224))(torch.rand(3, 100, 100))
    print('torchvision transform: OK')
except Exception as e:
    print('torchvision transform FAIL:', e)