import numpy as np
import matplotlib.pyplot as plt

N = 226

rhomax = 4.5


h = rhomax/N
rho = np.linspace(0,rhomax,N+1)

vec = np.zeros(N-1)

f = open("veconeelec.txt")
f.readline()

for i in range(len(vec)):
    line = f.readline()
    vec[i] = float(line)


plt.plot(rho[1:-1],abs(vec)**2)
plt.title("Egenvektor for et elektron")
plt.ylabel(r"u($\rho$)")
plt.xlabel(r"$\rho$")
plt.show()
