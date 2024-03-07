import numpy as np

# 1D
arr_1d_list = np.array([1, 2, 3])
arr_1d_tuple = np.array((1, 2, 3))
print(arr_1d_list.shape, arr_1d_tuple.shape)

# 2D
arr_2d_list = np.array([
    [1, 2, 3],
    [2, 3, 4]
])
arr_2d_tuple = np.array((
    (1, 2),
    (2, 3),
    (3, 4)
))
print(arr_2d_list.shape, arr_2d_tuple.shape)

# 3D
arr_3d_list = np.array([
    [[1, 2], [2, 3], [3, 4]],
    [[4, 5], [5, 6], [6, 7]]
])
print(arr_3d_list.shape)

# 4D
arr_4d_tuple = np.array((
    (((1, 1,), (1, 2)), ((1, 3), (1, 4)), ((1, 5), (1, 6))),
    (((2, 1,), (2, 2)), ((2, 3), (2, 4)), ((2, 5), (2, 6))),
    (((3, 1,), (3, 2)), ((3, 3), (3, 4)), ((3, 5), (3, 6))),
    (((4, 1,), (4, 2)), ((4, 3), (4, 4)), ((4, 5), (4, 6))),
))
print(arr_4d_tuple.shape)

# numpy.arange
arr1 = np.arange(10)
print(arr1, arr1.dtype)
arr2 = np.arange(1, 10, dtype=float)
print(arr2, arr2.dtype)
arr3 = np.arange(2, 3, 0.1)
print(arr3, arr3.dtype)
ref = np.array([[1, 2, 3], [3, 4, 5]])
arr4 = np.arange(10, like=ref)
print(ref)
print(ref.shape)

# linspace
# 生成一个包含在 [start, stop] 范围内的 5 个均匀分布的数字
values = np.linspace(0, 1, 5)
print("Generated Values:", values)

# 创建一个 3x3 的单位矩阵
identity_matrix_3x3 = np.eye(3)
print("3x3 Identity Matrix:")
print(identity_matrix_3x3)

# 创建一个 4x5 的单位矩阵
identity_matrix_4x5 = np.eye(4, 5)
print("\n4x5 Identity Matrix:")
print(identity_matrix_4x5)

# 创建一个 4x5 的单位矩阵,
identity_matrix_4x5_k2 = np.eye(4, 5, 2)
print("\n4x5 k=2 Identity Matrix:")
print(identity_matrix_4x5_k2)

# 创建一个 3x3 的单位矩阵，主对角线上偏移为 1
identity_matrix_offset_1 = np.eye(3, k=1)
print("\n3x3 Identity Matrix with Offset 1:")
print(identity_matrix_offset_1)

# 对焦矩阵
# 从一维数组创建对角矩阵
arr1 = np.array([1, 2, 3])
diag_matrix1 = np.diag(arr1)
print("Diagonal Matrix from 1D Array:")
print(diag_matrix1)

# 从二维数组获取主对角线元素
arr2 = np.array([[1, 0, 0], [0, 2, 0], [0, 0, 3]])
diag_elements = np.diag(arr2)
print("\nMain Diagonal Elements from 2D Array:")
print(diag_elements)

# 创建一个具有偏移的对角矩阵
arr3 = np.array([1, 2, 3, 4])
diag_matrix_offset = np.diag(arr3, k=1)
print("\nDiagonal Matrix with Offset:")
print(diag_matrix_offset)

# reshape
# 创建一个一维数组
arr1d = np.arange(12)
print("Original 1D Array:")
print(arr1d)

# 将一维数组变形为二维数组
arr2d = np.reshape(arr1d, (3, 4))
print("\nReshaped 2D Array:")
print(arr2d)

# 将二维数组展平为一维数组
arr_flat = np.reshape(arr2d, -1)
print("\nFlattened 1D Array:")
print(arr_flat)

# 创建一个三维数组
arr3d = np.arange(24).reshape((2, 3, 4))
print("\nOriginal 3D Array:")
print(arr3d)

# 将三维数组变形为二维数组
arr2d_from_3d = np.reshape(arr3d, (2, -1))
print("\nReshaped 2D Array from 3D:")
print(arr2d_from_3d)

### numpy.zeros
# 创建一个形状为 (2, 3) 的全零数组
zeros_array1 = np.zeros((2, 3))
print("2x3 Zero Array:")
print(zeros_array1)

# 创建一个形状为 (3, 3) 的全零整数数组
zeros_array2 = np.zeros((3, 3), dtype=int)
print("\n3x3 Integer Zero Array:")
print(zeros_array2)

# 创建一个形状为 (2, 2, 2) 的全零数组
zeros_array3 = np.zeros((2, 2, 2))
print("\n2x2x2 Zero Array:")
print(zeros_array3)

# 生成一个形状为 (2, 3) 的均匀分布随机样本
rand_array = np.random.rand(2, 3)
print(rand_array)

# 生成一个形状为 (2, 3) 的标准正态分布随机样本
randn_array = np.random.randn(2, 3)
print(randn_array)

# 生成一个形状为 (2, 3)、取值范围在 [1, 10) 的整数随机样本
randint_array = np.random.randint(1, 10, size=(2, 3))
print(randint_array)

# 创建一个数组并打乱顺序
original_array = np.arange(10)
np.random.shuffle(original_array)
print(original_array)