import numpy as np

# 创建一个数组
original_array = np.array([[1, 2, 3], [4, 5, 6]])

# 使用 numpy.copy 创建数组副本
copied_array = np.copy(original_array)

# 修改副本的值不影响原始数组
copied_array[0, 0] = 100

print("Original Array:")
print(original_array)

print("\nCopied Array:")
print(copied_array)
