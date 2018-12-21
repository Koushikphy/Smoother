import matplotlib.pyplot as plt 
from random import random 
import numpy as np, sys

n=5 #parameter of choice
x = np.arange(40)
y = np.log(x + 1) * np.exp(-x/8.) * x**2 + np.random.random(40) * 15
rft = np.fft.rfft(y)
print rft
rft[n:] = 0   # remove higher harmonics

y_smooth = np.fft.irfft(rft)

plt.plot(x, y, label='Original')
plt.plot(x, y_smooth, label='Smoothed')
plt.legend(loc=0).draggable()
plt.show()