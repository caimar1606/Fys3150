import numpy as np
import matplotlib.pyplot as plt

N = 251

omega = np.array([0.01,0.5,1,5])
vec = np.zeros((4,N-1))

rhomax = 18
rhomax2 = 10  #Trenger forskjellig rhomax for aa faa bra opplosning

rho = np.linspace(0,rhomax,N+1)
rho2 = np.linspace(0,rhomax2,N+1)

filenames = ["vectwoelec001.txt","vectwoelec05.txt","vectwoelec1.txt","vectwoelec5.txt"]
j = 0
for name in filenames:
    f = open(name)
    f.readline()
    for i in range(len(vec[0,:])):
        line = f.readline()
        vec[j,i] = float(line)
    j += 1

for i in range(len(filenames)-1):
    plt.plot(rho[1:-1],abs(vec[i,:])**2, linewidth = 2,label = r"$\omega_r = %g$" %(omega[i]))

plt.plot(rho2[1:-1],abs(vec[-1,:])**2,color = "k", linewidth = 2 ,label = r"$\omega_r$ = %g" %(omega[-1]))
plt.title("Plott av sannsynlighetstetthet for to elektroner")
plt.ylabel(r"|u($\rho$)|^2")
plt.xlabel(r"$\rho$")
plt.xscale("log")
plt.legend()
plt.show()
