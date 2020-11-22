import numpy as np
import matplotlib.pyplot as plt

font = {"family":"sans serif","weight" : "normal", "size": 15}
plt.rc("font",**font)
plt.rcParams.update({'figure.autolayout': True})

f = open("L40")

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


f = open("L60")

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


f = open("L80")

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


f = open("L100")

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
