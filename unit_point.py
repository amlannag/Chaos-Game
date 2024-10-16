#Draw N points for the chaos game 

import numpy as np 
import matplotlib.pyplot as plt

N = 3

r = np.arange(0,N)
points = np.exp(2.0*np.pi*1j*r/N)
print(points)

res = 100
w = np.arange(0,res)
unit_circle = np.exp(2.0*np.pi*w*1j/res)

start = np.random.randint(0,N)
start_point = points[start]

print(start)



plt.plot(np.real(unit_circle),np.imag(unit_circle),'b-')
plt.plot(np.real(points),np.imag(points),'r.')
plt.plot(np.real(start_point),np.imag(start_point), "g.")

plt.show()
print("End")