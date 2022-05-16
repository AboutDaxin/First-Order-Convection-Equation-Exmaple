# 4 / 1 / 2022
import matplotlib.pyplot as plt
import numpy as np
import os
from time import time

u = np.zeros((126, 101))
for j in range(0, 101):
    u[0, j] = (np.sin(np.pi*j*0.01))**40

for k in range(0, 125):
    for j in range(1, 100):
        u[k+1, j] = -0.008*(u[k, j]-u[k, j-1])/0.01 + u[k, j]
        u[k, 0] = u[k, 100] = 0

x = 0.01*np.arange(0, np.size(u, 1), 1)
for t in [0, 15, 25, 100]:
    plt.plot(x, u[t, :], label='t={0}'.format(t*0.008))
plt.title("$Question 3——Upwind Scheme$")
plt.legend()
plt.show()
