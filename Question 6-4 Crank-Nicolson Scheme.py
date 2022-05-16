# 4 / 1 / 2022
import matplotlib.pyplot as plt
import numpy as np
import os
from time import time

h=0.01
tao=0.008
H=int(1/h)
TAO=int(1/tao)

u = np.zeros((20*TAO+1, H+1))
for j in range(0, H+1):
    u[0, j] = (np.sin(np.pi*j*0.05))**40

for k in range(1, 20*TAO+1):
    u[k, 0] = u[k, H] = 0

r = H/(4*TAO)
U = [[] for i in range(20*TAO+1)]
U[0] = u[0, 1:H].T

upper_diag = np.ones((H-1, H-1))*r
center_diag = np.ones((H-1, H-1))
lower_diag = np.ones((H-1, H-1))*(-r)

A = np.eye(H-1)*center_diag
# 然后通过切片来修改上下两条对角线
np.fill_diagonal(A[:-1, 1:], upper_diag)
np.fill_diagonal(A[1:, :-1], lower_diag)

B = np.eye(H-1)*center_diag
np.fill_diagonal(B[:-1, 1:], lower_diag)
np.fill_diagonal(B[1:, :-1], upper_diag)

for k in range(20*TAO):
    U[k+1] = np.dot(np.dot(np.linalg.inv(A),B), U[k])


for k in range(1, 20*TAO+1):
    for j in range(1, H):
        u[k, j] = U[k][j-1]
        
x = h*np.arange(0, np.size(u, 1), 1)
for t in [0, 625, 1250, 2500]:
    plt.plot(x, u[t, :], label='t={0}'.format(t*tao))
plt.title('$Question 6-4——C-N Scheme$')
plt.legend()
plt.show()
