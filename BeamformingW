#Weights matrix calculation

import numpy

def mvdr_beamformer(H, X):
    W = numpy.zeros(H.shape,dtype=complex)
    num_sensors, N_fft=H.shape
    for freqBinIndex in range(N_fft-1,-1,-1):
        H_current = H[:, freqBinIndex].T
        P = X[:, :, freqBinIndex] + numpy.eye(num_sensors)
        numerator = numpy.dot(numpy.linalg.inv(P),H_current)
        denominator = numpy.dot(nominator.conj().T,H_current)
        W[:, freqBinIndex] = nominator / denominator
    return W
