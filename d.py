import numpy as np
import math

#################################
#  Steering vector calculating  #
#################################

def st_v(fs,N,d,ang,c):
    a = np.zeros(N, dtype=complex)

    b = 1j*2*math.pi*fs*d*np.sin(ang)/c
    
    for i in range(0,N):
        a[i]=np.exp(1j*i*2*math.pi*fs*d*np.sin(ang)/c)
    #print ('a = ')
    #print(a)
    #print(a.conj())
    return a


#####################################
#  Beamforming weights calculating  #
#####################################

def calcW(a,X):
    N = a.shape[0]
    W = np.zeros(N,dtype=complex)
    #R = np.cov(np.transpose(np.real(X)))
    R = np.dot(np.transpose(X),X)
    numerator = np.dot(np.linalg.inv(R),a)
    denominator = np.dot(-numerator.conj().T,a)    
    W = numerator / denominator
    return W

#####################################
#   Beamformed signal calculating   #
#####################################

def calcY(a,X):
    Y = np.dot(calcW(a,X).conj(),np.transpose(X))
    return Y


#####################################
#          Noise isolation          #
#####################################

def noise_est(a,X):
    N = a.shape[0]
    W = np.zeros(N,dtype=complex)
    R = np.cov(np.transpose(np.real(X)))
    numerator = np.dot(np.linalg.inv(R),a)
    denominator = np.dot(numerator.conj().T,a)    
    W = numerator / denominator
    noise = np.dot(W.conj(),np.transpose(X))
    return noise
