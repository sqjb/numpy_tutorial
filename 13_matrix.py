import numpy as np

# 创建两个矩阵
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# 矩阵乘法
result_dot = np.dot(matrix1, matrix2)
result_at = matrix1 @ matrix2

print("矩阵乘法（np.dot）:\n", result_dot)
print("矩阵乘法（@）:\n", result_at)


# 创建一个矩阵
matrix = np.array([[1, 2], [3, 4]])

# 矩阵转置
transposed_matrix1 = np.transpose(matrix)
transposed_matrix2 = matrix.T

print("矩阵转置（np.transpose）:\n", transposed_matrix1)
print("矩阵转置（.T）:\n", transposed_matrix2)


# 创建一个可逆矩阵
matrix = np.array([[1, 2], [3, 4]])

# 计算逆矩阵
inverse_matrix = np.linalg.inv(matrix)

print("原始矩阵:\n", matrix)
print("逆矩阵:\n", inverse_matrix)


# 创建一个矩阵
matrix = np.array([[1, 2], [3, 4]])

# 计算行列式
determinant = np.linalg.det(matrix)

print("原始矩阵:\n", matrix)
print("行列式:", determinant)