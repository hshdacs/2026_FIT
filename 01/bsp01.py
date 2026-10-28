import numpy as np
import matplotlib.pyplot as plt

a = [1,3,5,3]
b = [1,5,7,10]
delta = np.pi
t = np.linspace(-np.pi, np.pi, 300)
for i in range(0,4):
    x = np.sin(a[i] * t + delta)
    y = np.sin(b[i] * t)
    plt.subplot(2,2,i+1)
    plt.plot(x,y)
      
plt.show()