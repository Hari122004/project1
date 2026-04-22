import numpy as np
a = np.array([[1,2,3],[4,5,6]], dtype=np.int32)
print(a)
print(a.strides)

b = a.T
print(b)
print(b.strides)