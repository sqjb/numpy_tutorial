import numpy as np

# view操作
# 切片
arr = np.array([1, 2, 3, 4, 5, 6])
sliced_arr = arr[1:4]
print(sliced_arr.base is not None)

# transpose
transposed_arr = arr.T
print(transposed_arr.base is not None)

# reshape resize ravel
reshaped_arr = arr.reshape(3, 2)
print(reshaped_arr.base is not None)
resized_arr = np.resize(arr, (2, 6))
print(resized_arr.base is not None)

# copy
# 调用copy函数
sliced_arr_copy = arr.copy()
print(sliced_arr_copy.base is not None)

# 广播
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([10, 20, 30])
result = arr1 + arr2  # 创建原数组的副本来进行广播
print(result.base is not None)

# 高级索引
# 创建一个示例数组
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 使用整数数组进行高级索引
rows = np.array([0, 1, 2])
cols = np.array([0, 2, 1])
result1 = arr[rows, cols]
print("Integer Array Indexing:", result1)
print(result1.base is not None)

# 使用布尔数组进行高级索引
bool_index = arr > 4
result2 = arr[bool_index]
print("\nBoolean Array Indexing:", result2)
print(result2.base is not None)