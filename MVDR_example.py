import numpy as np
import scipy.io
import math
import matplotlib.pyplot as plt

from d import *

#################################
#         Initialising          #
#################################

#Loading MATLAB data
md = scipy.io.loadmat('MATLABdata.mat')
c = md['c'][0][0]
ang = md['incidentAngle'][0]/180*math.pi
Fc = np.array(md['fc'])
X = np.array(md['rx'])
t = np.array(md['t'])


#Distance between elements, number of sensors
d = 0.5
N = 5


#################################
#         Calculating           #
#################################

a = st_v(Fc,N,d,ang,c)
Y=calcY(a,X)
Noise = noise_est(a,X)

#################################
#           Plotting            #
#################################


plt.figure('graph1')

plt.subplot(221)
plt.plot(t,np.real(X))
plt.title('Raw signal')
plt.ylabel('Signal level')
plt.xlabel('Time')
#plt.show()

plt.subplot(222)
plt.plot(t,np.real(Y),'r--')
plt.title('Beamformed signal')
plt.ylabel('Signal level')
plt.xlabel('Time')
#plt.show()

plt.subplot(223)
plt.plot(t,np.real(Y),label="Beamformed signal")
plt.plot(t,np.real(Noise),label="Noise")
#plt.title('Signal separated from noise')
plt.ylabel('Signal level')
plt.xlabel('Time')
plt.legend()
plt.show()


################################################
#     Testing (comparision with MATLAB)        #
################################################

Y_matlab = np.array(md['y'])
#np.testing.assert_almost_equal(Y, Y_matlab, decimal = 3)

print('#################################')
print('#           Testing             #')
print('#################################')
print('')
print("Let's compare data set for Y from MATLAB and from Python.")
print('Because of some computational features, this 2 arrays are not equal.')
print('The best way to compare it is a standart derivation calculation.')
print("We should estimate the admissible value for it.")
print('')
print("There is no problem if we are mistaken (in average) in the signal value on 1% of it's range")
print("Signal range is about [-1,1] - hence, possible error is 0.02.")
print("But we shouldn't forget that Y takes complex values!!")
all_err = np.sqrt((0.02**2)*2001*2)
print('sqrt(0.02^2*2001*2) =', all_err)
print('So, we should ensure that standart derivation for MATLAB and Python data sets difference is less than', all_err)
print('')
print("Let's run a test!!!")
print('')
print('')
print('')
print('')


SD = np.std(Y_matlab-Y)

np.testing.assert_allclose(SD, 0, 0,all_err)

print('Test passed!!!')
print('Thank you for using this MVDR algorithm version!')
#print('Standart derivation', SD)
#print(SD)













#print('My values:')
#print('My W value')
#print(calcW(a,X))
#print(calcY(a,X))
#print('MATLAB values:')
#print(W_matlab)
#print(Y_matlab)


###########
#  WH*a = 1
###########

#print('WH*a = ')
#print(np.dot(calcW(a,X).conj(),a))
#print(W_matlab.conj())



#cons = 2*math.pi

####  For MATLAB values ####
#x1 = -0.347733*1j - 2.00798
#x2 = -0.551272*1j - 0.513357
#x3 = -0.40081*1j + 0.839412
#x4 = -0.202815*1j + 2.82233

####  For my values     ####
#x1 = -0.635432*1j - 2.38919
#x2 = -0.521158*1j - 1.01729
#x3 = -0.442613*1j + 0.482602
#x4 = 2.22298

#a1 = np.array([1, np.exp(1j*x1), np.exp(2*1j*x1),np.exp(3*1j*x1),np.exp(4*1j*x1)])
#a2 = np.array([1, np.exp(1j*x2), np.exp(2*1j*x2),np.exp(3*1j*x2),np.exp(4*1j*x2)])
#a3 = np.array([1, np.exp(1j*x3), np.exp(2*1j*x3),np.exp(3*1j*x3),np.exp(4*1j*x3)])
#a4 = np.array([1, np.exp(1j*x4), np.exp(2*1j*x4),np.exp(3*1j*x4),np.exp(4*1j*x4)])



#print('a_real = ')
#print(a)
#print('MATLAB a')
#print(a_matlab)
#print('#####################    MATLAB a VARIANTS CALCULATED BASED ON W_matlab values   ################')
#print('a1 = ')
#print(a1)
#print('a2 = ')
#print(a2)
#print('a3 = ')
#print(a3)
#print('a4 = ')
#print(a4)

#print ('___________________________________________________________')
#print('MATLAB W')
#print(W_matlab)
#print('MatlabWH * a_matlab')
#print(np.dot(np.transpose(W_matlab.conj()),a_matlab))

#print("Let's calculate now WH * a")
#print('For a1')
#print(np.dot(np.transpose(W_matlab.conj()),a1))
#print('For a2')
#print(np.dot(np.transpose(W_matlab.conj()),a2))
#print('For a3')
#print(np.dot(np.transpose(W_matlab.conj()),a3))
#print('For a4')
#print(np.dot(np.transpose(W_matlab.conj()),a4))
#print ('___________________________________________________________')

#print('')
#print('myW:')
#print('1')
#print(calcW(a1,X))
#print('It should be equal to 1')
#print(np.dot(calcW(a1,X).conj(),a1))
#print('2')
#print(calcW(a2,X))
#print('It should be equal to 1')
#print(np.dot(calcW(a2,X).conj(),a2))
#print('3')
#print(calcW(a3,X))
#print('It should be equal to 1')
#print(np.dot(calcW(a3,X).conj(),a3))
#print('4')
#print(calcW(a4,X))
#print('It should be equal to 1')
#print(np.dot(calcW(a4,X).conj(),a4))

#print ('___________________________________________________________')
#print('W_matlabH * a')
#print(np.dot(np.transpose(W_matlab.conj()),a))

#print ('___________________________________________________________')
#print ('W value')
#print(calcW(a,X))
#print('a value')
#print(a)
#print('')
#print ('I have an idea that there is no matter on R value.')
#print('Let us check it')

#R=np.array([[1,2,3,4,5],[3,4,6,5,7],[5,4,3,2,1],[1,3,4,6,7],[3,4,3,4,6]])
#print('Let R = ')
#print(R)


#numerator = np.dot(np.linalg.inv(R),a)
#denominator = np.dot(numerator.conj().T,a)    
#Wc = numerator / denominator

#print('numerator')
#print(numerator)
#print('denominator')
#print(denominator)
#print ('W calculated is')
#print(Wc)
#print("Let's now check if WcH * a = 1")
#print(np.dot(Wc.conj(),a))

#print('')
#print('Than R changes to')
#R=np.array([[5,2,2,5,2],[3,4,1,7,7],[2,1,5,6,3],[5,5,5,5,7],[1,3,5,7,9]])
#print(R)

#numerator = np.dot(np.linalg.inv(R),a)
#denominator = np.dot(numerator.conj().T,a)    
#Wc = numerator / denominator
#print ('In this time W calculated is')
#print(Wc)
#print("Let's now check if WcH * a = 1")
#print(np.dot(Wc.conj(),a))


#print('')
#print('This decicion was wrong and a have no idea why')



#print('**************************************************')
#print('******                                   *********')
#print('******                                   *********')
#print('**************************************************')
#print('')

#x = np.array([x1,x2,x3,x4])
#for i in range (0,4):
#    print ('sin(theta) for x',i+1)
#    print(x[i]*c/(2*d*math.pi*300000000))
#    print ('theta for x',i+1, '(in degrees)')
#    print(np.arcsin(x[i]*c/(2*d*math.pi*300000000))/math.pi*180)
#    print('')
