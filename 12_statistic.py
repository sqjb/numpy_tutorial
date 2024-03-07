import numpy as np

# 创建一个多维数组
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# 1. 平均值
mean_axis_0 = np.mean(arr_2d, axis=0)  # 沿着第一个轴计算平均值，即每列的平均值
mean_axis_1 = np.mean(arr_2d, axis=1)  # 沿着第二个轴计算平均值，即每行的平均值
print("平均值（轴0）:", mean_axis_0)
print("平均值（轴1）:", mean_axis_1)

# 2. 中位数
median_axis_0 = np.median(arr_2d, axis=0)
median_axis_1 = np.median(arr_2d, axis=1)
print("中位数（轴0）:", median_axis_0)
print("中位数（轴1）:", median_axis_1)

# 3. 总和
sum_axis_0 = np.sum(arr_2d, axis=0)
sum_axis_1 = np.sum(arr_2d, axis=1)
print("总和（轴0）:", sum_axis_0)
print("总和（轴1）:", sum_axis_1)

# 4. 最小值和最大值
min_axis_0 = np.min(arr_2d, axis=0)
min_axis_1 = np.min(arr_2d, axis=1)
max_axis_0 = np.max(arr_2d, axis=0)
max_axis_1 = np.max(arr_2d, axis=1)
print("最小值（轴0）:", min_axis_0)
print("最小值（轴1）:", min_axis_1)
print("最大值（轴0）:", max_axis_0)
print("最大值（轴1）:", max_axis_1)

# 5. 标准差和方差
std_axis_0 = np.std(arr_2d, axis=0)
std_axis_1 = np.std(arr_2d, axis=1)
var_axis_0 = np.var(arr_2d, axis=0)
var_axis_1 = np.var(arr_2d, axis=1)
print("标准差（轴0）:", std_axis_0)
print("标准差（轴1）:", std_axis_1)
print("方差（轴0）:", var_axis_0)
print("方差（轴1）:", var_axis_1)

# 6. 百分位数
percentile_50_axis_0 = np.percentile(arr_2d, 50, axis=0)
percentile_50_axis_1 = np.percentile(arr_2d, 50, axis=1)
print("百分位数(50%)（轴0）:", percentile_50_axis_0)
print("百分位数(50%)（轴1）:", percentile_50_axis_1)

