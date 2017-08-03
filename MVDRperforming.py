import numpy

#Arrival time delay
def td(sensor_positions, source_position, c, F_s):
	num_sensors = sensor_positions.shape[1]
	r_source = numpy.sqrt(numpy.sum(source_position**2,0))
	r_sensors_source=numpy.zeros((num_sensors,1))
	for sensor_index in range(num_sensors-1,-1,-1):
		r_sensors_source[sensor_index,0]=numpy.sqrt(numpy.sum((sensor_positions[:,sensor_index]-source_position)**2))
	T=(r_sensors_source-r_source) / c * F_s
	a=r_source / r_sensors_source
return T,a


   
#Beamforming object set    
def Set_object(sensor_positions, source_position, c, N_fft, F_s, theta):
    D = numpy.zeros((sensor_positions.shape[1],N_fft))
    D = D+0j
    T, a = td(sensor_positions, source_position, c, F_s)
    for sensor_index in range(sensor_positions.shape[1]-1, -1, -1):
        D[sensor_index, :] = a[sensor_index] * numpy.exp(-1j * theta * T[sensor_index])
return D



#Weights matrix calculation
def Weights_calc(H, X):
    W = numpy.zeros(H.shape,dtype=complex)
    num_sensors, N_fft=H.shape
    for decr in range(N_fft-1,-1,-1):
        HH = H[:, decr].T
        R = X[:, :, decr] + numpy.eye(num_sensors)
        numerator = numpy.dot(numpy.linalg.inv(R),HH)
        denominator = numpy.dot(nominator.conj().T,HH)
        W[:, decr] = nominator / denominator
    return W


#Output signal calculation
def out_sig(H,X)
    Y = numpy.dot(Weights_calc(H, X).conj(),X)
    return Y
