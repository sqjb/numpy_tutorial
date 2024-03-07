import ctypes
import numpy as np
# 创建两个变量，查看base
base = np.random.randint(256,size=12)
A = base.reshape(3,4)
B = base.reshape(2,6)
print(A.base is B.base)

# 创建一个随机的一维数组，例如长度为 10 的数组
random_array = np.random.rand(10)

# 使用 reshape 操作创建两个变量，分别具有不同的形状
reshaped_array1 = random_array.reshape(2, 5)  # 2行5列的数组
reshaped_array2 = random_array.reshape(5, 2)  # 5行2列的数组

# 打印原始数组的底层数据内存地址
original_data_address = ctypes.c_void_p(random_array.ctypes.data).value
print("Original Array Data Address:", original_data_address, random_array.data)

# 打印两个变量的底层数据内存地址
reshaped1_data_address = ctypes.c_void_p(reshaped_array1.ctypes.data).value
reshaped2_data_address = ctypes.c_void_p(reshaped_array2.ctypes.data).value
print("Reshaped Array 1 Data Address:", reshaped1_data_address, reshaped_array1.data)
print("Reshaped Array 2 Data Address:", reshaped2_data_address, reshaped_array2.data)

