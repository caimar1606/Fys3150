import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as inte

L=1
T=1

def f(x):
    return -1/L*x

def func(x,n):
    return f(x)*np.sin(n*np.pi/L*x)

def v(x,t):
    val = 0
    current = 1
    n = 1
    A=1
    while np.max(np.abs(current))>10**(-12):
        A = 2/(L)*inte.quad(func,0,L,args=(n))[0]
        current = A*np.sin(n*np.pi/L*x)*np.exp(-n**2*np.pi**2/(L**2)*t)
        val +=current
        n+=1
    return val


names = ["forward0_01dx","backward0_01dx","CN0_01dx"]

dx = 0.01

nx = 101
nt = 20001

x = np.linspace(0,L,nx)
t = np.linspace(0,T,nt)

dt = 0.00005
index = 5000
anal = v(x,dt*index)

for name in names:
    file = open(name)

    values = np.array([float(i) for i in file.read().split()]).reshape((nt,nx))

    plt.plot(x,values[index,:],label = "program")
    plt.plot(x,anal)
    plt.legend()
    plt.show()
    plt.plot(x,values[index]-f(x))
    plt.show()
