#Draw N points for the chaos game 

import numpy as np 
import matplotlib.pyplot as plt

N = 3

r = np.arange(0,N)
point = np.exp(2.0*np.pi*1j*r/N)
print(point)


res = 100
w = np.arange(0,res)
unit_circle = np.exp(2.0*np.pi*w*1j/res)

plt.plot(np.real(unit_circle),np.imag(unit_circle),'b-')
plt.plot(np.real(point),np.imag(point),'r.')

plt.show()
print("End")