#################################
#    Coordinates (positions)   #
#################################

import numpy as np


#Arrival time delay
def td(sensor_positions, source_position, c, F_s):
    num_sensors = sensor_positions.shape[1]
    r_source = np.sqrt(np.sum(np.square(source_position)))
    r_sensors_source=np.zeros((num_sensors,1))
    for sensor_index in range(num_sensors-1,-1,-1):
        r_sensors_source[sensor_index,0]=np.sqrt(np.sum((sensor_positions[:,sensor_index]-source_position)**2))
    T=(r_sensors_source-r_source) / c * F_s
    a=r_source / r_sensors_source
    return T,a

   
#Beamforming object set (based on coordinates)    
def set_object(sensor_positions, source_position, c, F_s, theta, N):
    H = np.zeros((sensor_positions.shape[1],N))
    H = H+0j
    T,a = td(sensor_positions, source_position, c, F_s)
    for sensor_index in range(sensor_positions.shape[1]-1, -1, -1):
        H[sensor_index, :] = a[sensor_index] * np.exp(-1j * theta * T[sensor_index])
    return H

#
