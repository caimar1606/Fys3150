#3b, calculating the velocity verlet method and forward euler without object orientation
#Programmed first in python, then wrote the object orientation code i cpp

import numpy as np
import matplotlib.pyplot as plt

N = 1000001 
T = 10                #slutttidspunkt

def forward(T, N):
    r = np.zeros((2,N))
    v = np.zeros((2,N))
    r[:,0] = [1,0]
    vel = np.sqrt(4*np.pi**2/np.linalg.norm(r[:,0]))
    v[:,0] = [0,vel]
    t = np.linspace(0,T,N)
    h = T/(N-1)
    for n in range(N-1):
        v[:,n+1] = v[:,n]-h*(4*np.pi**2/np.linalg.norm(r[:,n])**3)*r[:,n]
        r[:,n+1] = r[:,n] + h*v[:,n]

    return r, v, t

def velver(T, N):
    r = np.zeros((2,N))
    v = np.zeros((2,N))
    r[:,0] = [1,0]
    vel = np.sqrt(4*np.pi**2/np.linalg.norm(r[:,0]))
    v[:,0] = [0,vel]
    h = T/(N-1)
    for n in range(N-1):
        a1 = -(4*np.pi**2/np.linalg.norm(r[:,n])**3)*r[:,n]
        r[:,n+1] = r[:,n] + h*v[:,n]  + (h**2/2)*a1
        a2 = -(4*np.pi**2/np.linalg.norm(r[:,n+1])**3)*r[:,n+1]
        v[:,n+1] = v[:,n] + (h/2)*(a2+a1)

    return r, v

val = forward(T,N)
val2 = velver(T,N)

plt.plot(val[0][0], val[0][1], label = 'Forward Euler')
plt.plot(val2[0][0], val2[0][1],"k--", label = 'Velocity Verlet')
plt.axis('equal')
plt.legend()
plt.show()
