import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as inte

def f(x):
    return -1292/L*x-8

def func(x,n):
    return f(x)*np.sin(n*np.pi/L*x)

def u(x,t):
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


T = 10**9
Lplot = 120000
secconst = 3.16*pow(10,16)
nt = 50001
nx = 101



k = 2.5;
rho = 3.5*10*10*10;
cp = 1000;
gamma = np.sqrt(k/(rho*cp));
L = Lplot/gamma

t = np.linspace(0,T,nt)
xplot = np.linspace(0,Lplot,nx)
xscaled = xplot/gamma
dt = (t[1]-t[0])*secconst

index = [1000,5000,10000,-1]

file = open("noQ")

values = np.array([float(i) for i in file.read().split()]).reshape((nt,nx))

file = open("normalQ")

values2 = np.array([float(i) for i in file.read().split()]).reshape((nt,nx))

file = open("moreQ")

values3 = np.array([float(i) for i in file.read().split()]).reshape((nt,nx))

file = open("expQ")

values4 = np.array([float(i) for i in file.read().split()]).reshape((nt,nx))

fval = f(xscaled)

for i in range(len(index)):
    plt.plot(xplot-Lplot,values[index[i],:]-fval,label = index[i]*dt/secconst/(10**6))
plt.legend()
plt.show()
for i in range(len(index)):
    plt.plot(xplot-Lplot,values2[index[i],:]-fval,label = index[i]*dt/secconst/(10**6))
plt.legend()
plt.show()
for i in range(len(index)):
    plt.plot(xplot-Lplot,values3[index[i],:]-fval,label = index[i]*dt/secconst/(10**6))
plt.legend()
plt.show()
for i in range(len(index)):
    plt.plot(xplot-Lplot,values4[index[i],:]-fval,label = index[i]*dt/secconst/(10**6))
plt.legend()
plt.show()
