import numpy as np

np.random.seed(42)

a = np.array([[1,2,3],[4,5,6]])
b = np.array([10,20,30])
print(a + b)

c = np.arange(10)
print(c * 2)

d = np.array([10,20,30,40])
print(d[[0,2,3]])

print(d[d > 20])

e = np.arange(6)
print(e.reshape(2,3))
print(e.flatten())

f = np.array([1,2,3])
g = f.view()
g[0] = 99
print(f)

h = np.array([1,2])
i = np.array([3,4])
print(np.vstack((h,i)))
print(np.hstack((h,i)))

j = np.array([1,2,3,4])
print(np.split(j,2))

k = np.array([1,2,3])
print(np.sqrt(k))
print(np.exp(k))

l = np.array([[1,2],[3,4]])
print(np.linalg.det(l))
print(np.linalg.inv(l))
print(np.dot(l,l))

print(np.random.rand(2,2))
print(np.random.randint(1,10,5))
print(np.random.normal(0,1,5))

m = np.array([1,2,3], dtype=np.int8)
print(m.dtype)

n = np.arange(12).reshape(3,4)
print(n.T)

o = np.linspace(0,1,5)
print(o)

p = np.eye(3)
print(p)

q = np.zeros((2,3))
r = np.ones((2,3))
print(q)
print(r)

s = np.arange(1,10).reshape(3,3)
print(np.sum(s))
print(np.mean(s))
print(np.max(s))
print(np.min(s))

t = np.array([[1,2,3],[4,5,6]])
print(np.cumsum(t))
print(np.cumprod(t))

u = np.array([1,2,3])
v = np.array([4,5,6])
print(np.inner(u,v))
print(np.outer(u,v))

w = np.arange(16).reshape(4,4)
print(np.diag(w))
print(np.trace(w))

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
print(x @ y)

z = np.array([1,2,3,4,5])
print(np.where(z % 2 == 0, z, -1))

aa = np.array([1,2,3])
bb = np.copy(aa)
bb[0] = 100
print(aa)

print(np.__version__)
print(np.__file__)