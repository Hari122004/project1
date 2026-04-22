import numpy as np

np.random.seed(42)

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print(a @ b)
print(np.dot(a,b))

print(np.linalg.det(a))
print(np.linalg.inv(a))

eig_val, eig_vec = np.linalg.eig(a)
print(eig_val)
print(eig_vec)

A = np.array([[2,1],[1,3]])
B = np.array([8,13])
print(np.linalg.solve(A,B))

print(a.T)
print(np.linalg.matrix_rank(a))
print(np.trace(a))

print(np.random.rand(2,3))
print(np.random.randint(1,10,(2,3)))
print(np.random.normal(0,1,5))
print(np.random.uniform(0,10,5))

print(np.random.choice([10,20,30], size=5))

arr = np.array([1,2,3,4])
np.random.shuffle(arr)
print(arr)