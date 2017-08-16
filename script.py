#testing

import numpy as np
import matplotlib

from set_object import *
from out_sig import *

sensp = np.array([[1,2,3], [2,3,4], [4,5,6]])
sourp = [0,4,3]
c = 300000000
Fs = 3000000
ang = 1.1
N=3

H=set_object(sensp,sourp,c,Fs,ang,N)
X=np.array([[0.22,0.23,0.24,0.25,0.24,0.23,0.21], [0.25,0.26,0.27,0.28,0.28,0.26,0.25], [0.3,0.31,0.32,0.33,0.32,0.32,0.3]])
#Xsize is counts*n

#print(td(sensp,sourp,c,Fs))
print(set_object(sensp,sourp,c,Fs,ang,N))
#print(np.cov(X))
#print(weights_calc(H,X))
print(out_sig(H,X))
