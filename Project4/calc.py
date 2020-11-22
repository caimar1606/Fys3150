import numpy as np

T = 1.0
L = 2

z = (4*np.cosh(8)+12)
absM = (8/z)*(np.exp(8)+2)
E = (16/z)*2*np.cosh(8)
EE = (1/z)*2**8*np.cosh(8)


varme = (1/T**2)*EE-E**2

sus = (32*np.exp(8)+32)/z

print('Z = %f' %(z))
print('<E> = %g' %(E/L**2))
print('|M| = %f' %(absM/L**2))
print('Varmekapasiteten Cv er %f' %(varme/L**2))
print('Suscebiliteten er %f' %(sus/L**2))
