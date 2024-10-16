#Draw N points for the chaos game 

import numpy as np 
import matplotlib.pyplot as plt

N = 100

r = np.arange(0,N)
points = np.exp(2.0*np.pi*1j*r/N)
print(points)

res = 100
w = np.arange(0,res)
unit_circle = np.exp(2.0*np.pi*w*1j/res)

pick = np.random.randint(0,N)
pick_point = points[pick]

start = 0.1 +0.5j

#compute mid point
vector = (pick_point - start)/2.0
new_point = start + vector 

print(start)



plt.plot(np.real(unit_circle),np.imag(unit_circle),'b-')
plt.plot(np.real(points),np.imag(points),'r.')
plt.plot(np.real(pick_point),np.imag(pick_point), "g.")
plt.plot(np.real(start),np.imag(start), "y.")
plt.plot(np.real(new_point),np.imag(new_point), "m.")
plt.show()
print("End")