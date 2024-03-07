import numpy as np

# 一维数组转二维数组
arr1d = np.array([1, 2, 3, 4, 5, 6])
arr2d = np.reshape(arr1d, (2, 3))
print(arr2d)

# 二维数组转一维数组
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
arr1d = np.reshape(arr2d, (6,))
print(arr1d)

# 改变数组的维度
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = np.reshape(arr, (2, 3))  # 使用Fortran（列优先）顺序
print(reshaped_arr)

# 多维数组的形状改变
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
reshaped_arr = np.reshape(arr, (2, 3, 2))
print(reshaped_arr)

# 使用-1自动计算维度
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = np.reshape(arr, (2, -1))  # -1表示由数组自动计算
print(reshaped_arr)