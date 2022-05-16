# 4 / 1 / 2022
import matplotlib.pyplot as plt
import numpy as np
import os
from time import time

u = np.zeros((26, 21))
for j in range(0, 21):
    u[0, j] = (np.sin(np.pi*j*0.05))**40

for k in range(0, 25):
    for j in range(1, 20):
        u[k+1, j] = -0.04*(u[k, j]-u[k, j-1])/0.05 + u[k, j]
        u[k, 0] = u[k, 20] = 0

x = 0.05*np.arange(0, np.size(u, 1), 1)
for t in [0, 3, 5, 20]:
    plt.plot(x, u[t, :], label='t={0}'.format(t*0.04))
plt.title("$Question 2——Upwind Scheme$")
plt.legend()
plt.show()
