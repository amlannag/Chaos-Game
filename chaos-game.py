#Draw N points for the chaos game 

import numpy as np 
import matplotlib.pyplot as plt

N = 3

r = np.arange(0,N)
points = np.exp(2.0*np.pi*1j*r/N)
print(points)

res = 1000
w = np.arange(0,res)
unit_circle = np.exp(2.0*np.pi*w*1j/res)

start = 0.1 +0.5j

def computer_new_rand_location(startLoc):
    rand_location = np.random.randint(0,N)
    vector =(points[rand_location]- startLoc)/2.0
    new_point = startLoc + vector
    return new_point, points[rand_location]




plt.plot(np.real(unit_circle),np.imag(unit_circle),'b-')
plt.plot(np.real(points),np.imag(points),'r.')

next_point = start
for iteraetion in range(100):
    next_point, rand_location = computer_new_rand_location(next_point)
    plt.plot(np.real(next_point),np.imag(next_point),"b.")


plt.show()
print("End")