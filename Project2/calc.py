import numpy as np
import matplotlib.pyplot as plt

N = 101

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
numeig = np.zeros(N-1)
numvec = np.zeros(N-1)


f = open("buckbeam.txt")
f.readline()
for i in range(0,len(numvec)):
    numeig[i]=float(f.readline())
f.close()

print(numeig[:6])
print(val[:6])

plt.plot(rho[1:-1],numeig,"b-",label = "Jacobi",linewidth =3)
plt.plot(rho[1:-1],val,"y--",label = "Analytical", linewidth = 2)
plt.xlim(0,1)
plt.ylim(0,np.max(numeig)+100)
plt.title("Egenverdier for Jacobimetoden og analytiske for Buckling Beam")
plt.xlabel(r"$\rho$")
plt.ylabel(r"$\lambda$")
plt.legend(loc = "lower right")
plt.show()

f = open("vecbuckbeam.txt")
f.readline()
for i in range(N-1):
    numvec[i] = float(f.readline())


plt.plot(rho[1:-1],numvec,label = "Jacobi")
plt.plot(rho[1:-1],vec[0,:],label = "Analytical")
plt.xlim(0,1)
plt.ylim(0,np.max(vec[0,:])+0.1)
plt.title("Egenvektor nr 1 for Jacobimetoden og analytisk Buckling Beam")
plt.xlabel(r"$\rho$")
plt.ylabel(r"u($\rho$)")
plt.legend()
plt.show()

numvec = numvec/np.linalg.norm(numvec)
scalevec = vec[0,:]/np.linalg.norm(vec[0,:])

plt.plot(rho[1:-1],numvec,label = "Jacobi")
plt.plot(rho[1:-1],scalevec,label = "Analytical", linestyle = "dashed",color = "k", linewidth = 2)
plt.title("Egenvektor nr 1 for Jacobimetoden og normalisert, analytisk Buckling Beam")
plt.xlabel(r"$\rho$")
plt.ylabel(r"u($\rho$)")
plt.xlim(0,1)
plt.ylim(0,np.max(scalevec)+0.01)
plt.legend()
plt.show()
