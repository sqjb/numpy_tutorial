import numpy as np

angle = np.pi / 2 # 角度，以弧度为单位

# 正弦
sin_value = np.sin(angle)
print("sin(", angle, ") =", sin_value)

# 余弦
cos_value = np.cos(angle)
print("cos(", angle, ") =", cos_value)

# 正切
tan_value = np.tan(angle)
print("tan(", angle, ") =", tan_value)

# 反正弦
angle = np.arcsin(sin_value)
print("arcsin(", sin_value, ") =", angle)

# 反余弦
angle = np.arccos(cos_value)
print("arccos(", cos_value, ") =", angle)

# 反正切
angle = np.arctan(tan_value)
print("arctan(", tan_value, ") =", angle)

# 弧度和角度转换
angle_in_degrees = 45
angle_in_radians = np.radians(angle_in_degrees)
print(angle_in_degrees, "degrees in radians:", angle_in_radians)

angle_in_radians = np.pi / 4
angle_in_degrees = np.degrees(angle_in_radians)
print(angle_in_radians, "radians in degrees:", angle_in_degrees)


datas = np.array([-0.5, 0.1, 1.5, 2.5, 2.15, 3.6])
results = np.round(datas)
print("data:\n",datas)
print("round:\n", results)

datas = np.array([-0.5, 0.1, 1.5, 2.5, 2.15, 3.6])
results1 = np.around(datas)
print("data:\n",datas)
print("around:\n", results1)

import numpy as np

x = 3.99
floor_value = np.floor(x)
print("Floor value:", floor_value)

x = 3.01
ceil_value = np.ceil(x)
print("Ceiling value:", ceil_value)

x = -3.99
trunc_value = np.trunc(x)
print("Truncated value:", trunc_value)

# 创建一个包含一些数值的NumPy数组
arr = np.array([2, 0.5, 4, 8])

# 使用 np.reciprocal() 计算数组元素的倒数
reciprocal_arr = np.reciprocal(arr)

# 打印结果
print("原始数组:", arr)
print("元素的倒数:", reciprocal_arr)


# 创建一个包含一些数值的NumPy数组
arr = np.array([1, 2, 3, 4])

# 使用 np.exp() 计算数组元素的指数
exp_arr = np.exp(arr)

# 打印结果
print("原始数组:", arr)
print("元素的指数:", exp_arr)

import numpy as np

# 创建两个包含一些数值的 NumPy 数组
arr1 = np.array([7, -13, 13, 19])
arr2 = np.array([2, 5, -5, 7])

# 使用 np.remainder() 计算数组元素的余数
remainder_arr = np.remainder(arr1, arr2)
mod_arr = np.mod(arr1, arr2)
_arr = arr1 % arr2
# 打印结果
print("arr1:", arr1)
print("arr2:", arr2)
print("元素的余数(remainder):", remainder_arr)
print("元素的余数(mod):", mod_arr)
print("元素的余数(%):", _arr)
