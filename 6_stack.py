import numpy as np

# concatenate
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
# concatenate
c1 = np.concatenate((a, b))
c2 = np.concatenate((a, b), axis=1)
# print(np.concatenate((a, b)))
# print(np.concatenate((a,b),axis=1))

# stack
# axis = 0
s1 = np.stack((a, b))
print(f"stack((a,b)): shape-{s1.shape}")
print(s1)

# axis = 1
s2 = np.stack((a, b), axis=1)
print(f"stack((a,b), axis=1): shape-{s2.shape}")
print(s2)

# axis = 2
s3 = np.stack((a, b), axis=2)
print(f"stack((a,b), axis=2): shape-{s3.shape}")
print(s3)

# axis = 1: reshape and concatenate
reshaped_a = a.reshape(3, 1, 3)
print("a:\n",a)
print("reshaped_a:\n", reshaped_a)
reshaped_b = b.reshape(3, 1, 3)
c = np.concatenate((reshaped_a, reshaped_b), axis=1)
print("reshape and concatenate:")
print(c)

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
# (3,3) + (3,3) = (6, 3)
v1 = np.vstack((a,b))
print(v1)

# (3,3) + (3,) = (4,3)
c = np.array([0,0,0])
v2 = np.vstack((a,c))
print(v2)

print("hstack examples:\n")
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
h1 = np.hstack((a,b))
print(h1)

c = np.array([[0],[0],[0]])
h2 = np.hstack((a,c))
print(h2)
