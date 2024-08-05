#Draw N points for the chaos game 

import numpy as np 

N = 3

r = np.arange(0,N)
point = np.exp(2.0*np.pi*1j*r/N)
print(point)