import ctypes

import numpy as np

# 创建随机数组
a = np.random.randint(256, size=1280*720*3).reshape(1280,720,3)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)
print(a.itemsize)
print(a.base)

b = np.array([1,2,3])
print(b.base)
print(type(b))
