# Fake tide chart generator

import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 18, 1000)
y_vals = 2 * np.cos(2 * np.pi * x / 12)


plt.plot(x, y_vals)
plt.xlabel('Hour')
plt.ylabel('Tide Height')
plt.axhline(y=0, color='red', linestyle='--')
plt.show()
