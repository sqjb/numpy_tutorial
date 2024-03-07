import numpy as np

# 创建一维向量
vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])

print("向量 A:", vector_a)
print("向量 B:", vector_b)

result_addition = vector_a + vector_b
print("向量相加结果:", result_addition)

result_subtraction = vector_a - vector_b
print("向量相减结果:", result_subtraction)

scalar = 2
result_scalar_multiply = vector_a * scalar
print("向量标量乘法结果:", result_scalar_multiply)

dot_product_result = np.dot(vector_a, vector_b)
# 或者使用 @ 运算符
# dot_product_result = vector_a @ vector_b

print("向量点乘结果:", dot_product_result)

cross_product_result = np.cross(vector_a, vector_b)
print("向量叉乘结果:", cross_product_result)
