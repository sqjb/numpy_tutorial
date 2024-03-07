import numpy as np

arr = np.array([1, 2, 3, 4, 5])
indices = np.array([1, 3, 4])

result = arr[indices]
print(result)

# 创建一个2D数组
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# 整数数组索引：选择特定行
row_indices = np.array([0, 2])
selected_rows = arr_2d[row_indices, :]
print("Selected Rows:")
print(selected_rows)
print("is view:", selected_rows.base is None)

# 整数数组索引：选择特定列
col_indices = np.array([1, 2])
selected_cols = arr_2d[:, col_indices]
print("\nSelected Columns:")
print(selected_cols)
print("is view:", selected_cols.base is None)

# 布尔数组索引：根据条件选择元素
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
bool_mask = arr_2d > 4
print("bool_mask:\n", bool_mask)
selected_elements = arr_2d[bool_mask]
print("\nSelected Elements (based on condition):")
print(selected_elements)

# 筛选总和小于60的行
x = np.arange(24).reshape(4, 6)
print("原始数组:\n", x)

bool_mask = (x.sum(1) <= 60)
print("筛选数组:\n", bool_mask)

selected_rows = x[bool_mask,]
print("筛选后的数组:\n", selected_rows)
