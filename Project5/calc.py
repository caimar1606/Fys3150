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


names = ["forward0_1dx","backward0_1dx","CN0_1dx"]
algo = ['Forward Euler', 'Backward Euler', 'Crank-Nicholsen']
names2 = ['forward0_01dx', 'backward0_01dx','CN0_01dx']

dx = 0.1

nx = 11
nt = 201
x = np.linspace(0,L,nx)
t = np.linspace(0,T,nt)

dt = t[1]-t[0]
index = [10,40]

for i in range(len(index)):
    anal = v(x,dt*index[i])
    for j in range(len(names)):
        file = open(names[j])

        values = np.array([float(k) for k in file.read().split()]).reshape((nt,nx))
        plt.plot(x,values[index[i],:],label = "program")
        plt.plot(x,anal)
        plt.legend()
        plt.show()
        plt.plot(x,values[index[i]]-f(x))
        plt.show()

        print('Differansen mellom den analytiske og den simulerte løsningen i %s er %g ved t = %g' %(algo[j],np.average(np.abs(anal-values[index[i],:])),index[i]*dt))



dx = 0.01

nx = 101
nt = 20001
x = np.linspace(0,L,nx)
t = np.linspace(0,T,nt)

dt = t[1]-t[0]
index = [1000,4000]

for i in range(len(index)):
    anal = v(x,dt*index[i])
    for j in range(len(names2)):
        file = open(names2[j])
        values = np.array([float(k) for k in file.read().split()]).reshape((nt,nx))
        plt.plot(x,values[index[i],:],label = "program")
        plt.plot(x,anal)
        plt.legend()
        plt.show()
        plt.plot(x,values[index[i]]-f(x))
        plt.show()
        print('Differansen mellom den analytiske og den simulerte løsningen i %s er %g ved t = %g' %(algo[j],np.average(np.abs(anal-values[index[i],:])),index[i]*dt))
