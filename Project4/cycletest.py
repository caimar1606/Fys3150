import numpy as np
import matplotlib.pyplot as plt


T = 1.0
L = 2

z = (4*np.cosh(8)+12)
absMexact = (8/z)*(np.exp(8)+2)
Eexact = (16/z)*2*np.cosh(8)
EE = (1/z)*2**8*np.cosh(8)


varme = (1/T**2)*EE-Eexact**2

susexact = (32*np.exp(8)+32)/z

print('Z = %f' %(z))
print('<E> = %g' %(Eexact/L**2))
print('|M| = %f' %(absMexact/L**2))
print('Varmekapasiteten Cv er %f' %(varme/L**2))
print('Suscebiliteten er %f' %(susexact/L**2))
