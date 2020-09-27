import numpy as np
import matplotlib.pyplot as plt

def eigenval(omega_r, m):
    V_0 = (3./2)*(omega_r/2)**(2./3)
    omegae = np.sqrt(3)*omega_r
    val = V_0+omegae*(m+(1./2))
    val = val*(2.*omega_r**2)**(-1./3)
    return val

N = 150
m = np.linspace(0, N, N+1)
omega_r = 0.05


eigenvalues = eigenval(omega_r, m)
print(eigenvalues)
#plt.plot(m, eigenvalues)
#plt.show()
