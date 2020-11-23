"""
Dette programmet regner ut temperaturverdier for overganger for forskjellige L-verdier.
Etterpå gjør den in linearregressjon for å finne overgangstemperaturen når L går mot uendelig.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

L = np.array([40,60,80,100])

Tmincv = np.array([2.280, 2.270, 2.270, 2.265 ])
Tmaxcv = np.array([2.305, 2.295, 2.290, 2.285])
Tminsus = np.array([2.310, 2.295,2.285, 2.285])
Tmaxsus = np.array([2.330,2.310, 2.305, 2.295])

Tcv = (Tmincv+Tmaxcv)/2
dTcv = (Tmaxcv-Tmincv)/2

Tsus = (Tminsus+Tmaxsus)/2
dTsus = (Tmaxsus-Tminsus)/2

Toploc = (Tcv+Tsus)/2

Toploc[3] = Toploc[3]
dToploc = np.sqrt((dTcv/Tcv)**2+(dTsus/Tsus)**2)

for i in range(len(Toploc)):
    print("Toppene er plassert ved T = %.3f +- %.3f" %(Toploc[i],dToploc[i]))

values = stats.linregress(1.0/L,Toploc)

print("Den kritiske temperaturen er ved %.3f" %(values[1]))
