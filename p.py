# coding: utf-8

import numinger as nu
import numpy as np
import matplotlib.pyplot as plt

D = nu.Domain(-1, 1, 1000)
#V = np.zeros(len(D))
#V[0] = 1e15
#V[-1] = 1e15
V = 0.5*D.as_array()**2
print(V)

ev, ef = nu.schrod(D, V, 1, 1, eigen_num=5)

for v, f in zip(ev, ef):
    plt.plot(D.as_array(), f, label="{:.4}".format(v))

plt.grid(True)
plt.legend()
plt.show()
