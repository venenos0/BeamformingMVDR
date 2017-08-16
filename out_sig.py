import numpy as np

#Weights matrix calculation
def weights_calc(H, X):
    W = np.zeros(H.shape,dtype=complex)
    num_sensors, N = H.shape
    
    R=np.cov(X)
    
    for decr in range(N-1,-1,-1):
        HH = H[:, decr].T
        #R = X[:, decr] + np.eye(num_sensors)
        numerator = np.dot(np.linalg.inv(R),HH)
        denominator = np.dot(numerator.conj().T,HH)
    #W[:, decr] = numerator / denominator
    W=numerator/denominator
    return W

#Output signal calculation
def out_sig(H, X):
    Y = np.dot(weights_calc(H, X).conj(),X)
    return Y
