import numpy as np
import matplotlib.pyplot as plt

N = 100

def lamb(N):
    rho_N  = 1.0
    rho_0 = 0.0
    h = (rho_N - rho_0)/N
    d = 2./(h**2)
    a = -1./(h**2)
    eigenvals  = np.zeros(N-1)
    eigenvec = np.zeros((N-1,N-1))
    for j in range(1,len(eigenvals)+1):
        eigenvals[j-1] = d+(2*a*np.cos((j*np.pi)/N))
        eigenvec[j-1,:] = np.array([np.sin(i*j*np.pi/N) for i in range(1,N)])
    return eigenvals,eigenvec

val,vec = lamb(N)

rho = np.linspace(0,1,N+1)
numvec = np.zeros(N-1)

f = open("2b.txt")
f.readline()
f.readline()
for i in range(0,len(numvec)):
    numvec[i]=float(f.readline())

plt.plot(rho[1:-1],numvec,label = "Jacobi")
plt.plot(rho[1:-1],vec[0,:],label = "Analytical")
plt.xlim(0,1)
plt.ylim(0,np.max(vec[0,:])+0.1)
plt.title("Jacobi vs Analytical")
plt.xlabel(r"$\rho$")
plt.ylabel("y")
plt.legend()
plt.show()

numvec = numvec/np.linalg.norm(numvec)
scalevec = vec[0,:]/np.linalg.norm(vec[0,:])

plt.plot(rho[1:-1],numvec,label = "Jacobi")
plt.plot(rho[1:-1],scalevec,label = "Analytical", linestyle = "dashed",color = "k", linewidth = 2)
plt.title("Jacobi vs Analytical, scaled")
plt.xlabel(r"$\rho$")
plt.ylabel("y")
plt.xlim(0,1)
plt.ylim(0,np.max(scalevec)+0.01)
plt.legend()
plt.show()
