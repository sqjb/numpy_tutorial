import numpy as np

a = np.arange(24).reshape(2, 3, 4)
# 不带切片
print(a[0])
print(a[0, ])

print(a[0][1])
print(a[0, 1])

print(a[0][1][2])
print(a[0, 1, 2])
print(a[0][1, 2])

# 一维切片
a = np.arange(10)
print(a)
s1 = a[1:5:2]
print(s1)

# 多维切片
b = np.arange(24).reshape(4,3,2)
print(b)
s2 = b[1:3:1]
print(s2)

# 多维同时索引
s3 = b[:,1:3,...]
print(s3)

