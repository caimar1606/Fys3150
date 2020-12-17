import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as inte

def analytic(x,y,t,nmax,mmax):
    val = np.zeros((len(x),len(x)))
    current = np.zeros((len(x),len(x)))
    A=1
    n=1
    m=1
    current = 1

    XX,YY = np.meshgrid(x,y)
    while(n<nmax and m<mmax):
        A = 4/(X**2)*inte.dblquad(func,0,X,0,X,args=(n,m))[0]
        current = A*np.sin(n*np.pi/X*XX)*np.sin(m*np.pi/X*YY)*np.exp(-(n**2+m**2)*np.pi**2/(X**2)*t)
        val += current
        if n<=m:
            n+=1
        else:
            m+=1

    return val

def func(y,x,n,m):
    return np.sin(np.pi/X*x)*np.sin(np.pi/X*y)*np.sin(n*np.pi/X*x)*np.sin(m*np.pi/X*y)

X = 1
T = 1
nx = 51
nt = 201

x = np.linspace(0,X,nx)
t = np.linspace(0,T,nt)

dt = t[1]-t[0]

index = np.array([0,10,20,30])

f = open("2d")

values = np.array([float(i) for i in f.read().split()]).reshape((nt,nx,nx))

for i in index:
    anal = analytic(x,x,i*dt,30,30)
    plt.contourf(x,x,values[i])
    plt.title("Sim")
    plt.colorbar()
    plt.show()

    plt.contourf(x,x,anal)
    plt.colorbar()
    plt.title("anal")
    plt.show()

    plt.plot(x,values[i,nx//2,:],label = "sim")
    plt.plot(x,anal[nx//2,:],label = "anal")
    plt.legend()
    plt.show()
