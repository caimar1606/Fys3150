"""
Dette programmet plotter forventingsverdier for energi, varmekapasitet, abs(magnetisk moment)
og magnetisk susceptibilitet for forskjellige L-verdier over forskjellige temperatur intervaller
"""
import numpy as np
import matplotlib.pyplot as plt

font = {"family":"sans serif","weight" : "normal", "size": 15}
plt.rc("font",**font)
plt.rcParams.update({'figure.autolayout': True})


#Plott av verdier for L = 40
f = open("runs/peaksims/L40")

words = f.read().split()

values = [float(i) for i in words]

T = np.array(values[0::6])
E = values[1::6]
Cv = np.array(values[2::6])
M = values[3::6]
absM = values[4::6]
Sus = values[5::6]

plt.title(r'Forventingsverdien $\langle E \rangle$ mot temperaturen T ved L = 40')
plt.ylabel(r'$\langle E \rangle$', fontsize=20)
plt.xlabel('T', fontsize=20)
plt.plot(T,E)
plt.show()

plt.title(r'Forventningsverdien $\langle C_v \rangle$ mot temperaturen T ved L = 40')
plt.ylabel(r'$\langle C_v \rangle $', fontsize=20)
plt.xlabel('T', fontsize=20)
plt.plot(T,Cv*T)
plt.show()

plt.title(r'Forventningsverdien $\langle |M|\rangle$ mot temperaturen T ved L = 40')
plt.ylabel(r'$\langle |M|\rangle $', fontsize=20)
plt.xlabel('T', fontsize=20)
plt.plot(T,absM)
plt.show()

plt.title(r'Forventningsverdien $\langle \chi \rangle$ mot temperaturen T ved L = 40')
plt.ylabel(r'$\langle \chi \rangle $', fontsize=20)
plt.xlabel('T', fontsize=20)
plt.plot(T,Sus)
plt.show()

#Plott av verdier for L=60
f = open("runs/peaksims/L60")

words = f.read().split()

values = [float(i) for i in words]

T = np.array(values[0::6])
E = values[1::6]
Cv = np.array(values[2::6])
M = values[3::6]
absM = values[4::6]
Sus = values[5::6]

plt.title(r'Forventingsverdien $\langle E \rangle$ mot temperaturen T ved L = 60')
plt.ylabel(r'$\langle E \rangle$', fontsize=20)
plt.xlabel('T', fontsize=20)
plt.plot(T,E)
plt.show()

plt.title(r'Forventningsverdien $\langle C_v \rangle$ mot temperaturen T ved L = 60')
plt.ylabel(r'$\langle C_v \rangle $', fontsize=20)
plt.xlabel('T', fontsize=20)
plt.plot(T,Cv*T)
plt.show()

plt.title(r'Forventningsverdien $\langle |M|\rangle$ mot temperaturen T ved L = 60')
plt.ylabel(r'$\langle |M|\rangle $', fontsize=20)
plt.xlabel('T', fontsize=20)
plt.plot(T,absM)
plt.show()

plt.title(r'Forventningsverdien $\langle \chi \rangle$ mot temperaturen T ved L = 60')
plt.ylabel(r'$\langle \chi \rangle $', fontsize=20)
plt.xlabel('T', fontsize=20)
plt.plot(T,Sus)
plt.show()

#Plott av verdier for L = 80
f = open("runs/peaksims/L80")

words = f.read().split()

values = [float(i) for i in words]

T = np.array(values[0::6])
E = values[1::6]
Cv = np.array(values[2::6])
M = values[3::6]
absM = values[4::6]
Sus = values[5::6]

plt.title(r'Forventingsverdien $\langle E \rangle$ mot temperaturen T ved L = 80')
plt.ylabel(r'$\langle E \rangle$', fontsize=20)
plt.xlabel('T', fontsize=20)
plt.plot(T,E)
plt.show()

plt.title(r'Forventningsverdien $\langle C_v \rangle$ mot temperaturen T ved L = 80')
plt.ylabel(r'$\langle C_v \rangle $', fontsize=20)
plt.xlabel('T', fontsize=20)
plt.plot(T,Cv*T)
plt.show()

plt.title(r'Forventningsverdien $\langle |M|\rangle$ mot temperaturen T ved L = 80')
plt.ylabel(r'$\langle |M|\rangle $', fontsize=20)
plt.xlabel('T', fontsize=20)
plt.plot(T,absM)
plt.show()

plt.title(r'Forventningsverdien $\langle \chi \rangle$ mot temperaturen T ved L = 80')
plt.ylabel(r'$\langle \chi \rangle $', fontsize=20)
plt.xlabel('T', fontsize=20)
plt.plot(T,Sus)
plt.show()

#Plott av verdier for L = 100
f = open("runs/peaksims/L100")

words = f.read().split()

values = [float(i) for i in words]

T = np.array(values[0::6])
E = values[1::6]
Cv = np.array(values[2::6])
M = values[3::6]
absM = values[4::6]
Sus = values[5::6]

plt.title(r'Forventingsverdien $\langle E \rangle$ mot temperaturen T ved L = 100')
plt.ylabel(r'$\langle E \rangle$', fontsize=20)
plt.xlabel('T', fontsize=20)
plt.plot(T,E)
plt.show()

plt.title(r'Forventningsverdien $\langle C_v \rangle$ mot temperaturen T ved L = 100')
plt.ylabel(r'$\langle C_v \rangle $', fontsize=20)
plt.xlabel('T', fontsize=20)
plt.plot(T,Cv*T)
plt.show()

plt.title(r'Forventningsverdien $\langle |M|\rangle$ mot temperaturen T ved L = 100')
plt.ylabel(r'$\langle |M|\rangle $', fontsize=20)
plt.xlabel('T', fontsize=20)
plt.plot(T,absM)
plt.show()

plt.title(r'Forventningsverdien $\langle \chi \rangle$ mot temperaturen T ved L = 100')
plt.ylabel(r'$\langle \chi \rangle $', fontsize=20)
plt.xlabel('T', fontsize=20)
plt.plot(T,Sus)
plt.show()
