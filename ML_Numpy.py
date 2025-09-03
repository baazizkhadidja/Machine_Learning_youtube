import numpy as np


A = np.array([1, 2, 3])
A.shape

B = np.zeros((3,2))
B.ndim
B.shape

C = np.ones((3, 5))

C.size

D = np.full((2, 3), 9)
D

arr = np.random.randn(3, 4)

notes = np.random.normal(loc=12, scale=2, size=100)

np.eye(4)

np.linspace(0, 10, 20, dtype=np.float16 )



A= np.zeros((3,2))

B = np.ones((3, 2))

print(A)

print(B)

C1 = np.hstack((A,B))
C1

C2 = np.vstack((A, B))
C2

C3 = np.concatenate((A, B), axis=0)
C3
C4 = np.concatenate(, ()