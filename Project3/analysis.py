import numpy as np
import matplotlib.pyplot as plt

font = {"family":"sans serif","weight" : "normal", "size": 13}
plt.rc("font",**font)
plt.rcParams.update({'figure.autolayout': True})

f = open("Euler_position_object_0.txt","r")

f.readline()
words = f.read().split()
for i in range(len(words)):
    words[i] = float(words[i])
xstar = np.array(words[::2])
ystar = np.array(words[1::2])

f.close()

f = open("Euler_position_object_1.txt","r")

f.readline()
words = f.read().split()
for i in range(len(words)):
    words[i] = float(words[i])
xplanet = np.array(words[::2])
yplanet = np.array(words[1::2])

plt.plot(xplanet-xstar,yplanet-ystar)
#plt.plot(xstar,ystar)
plt.axis("equal")
plt.show()

f = open("verlet_position_object_0.txt","r")

f.readline()
words = f.read().split()
for i in range(len(words)):
    words[i] = float(words[i])
xstar = np.array(words[::2])
ystar = np.array(words[1::2])

f.close()

f = open("verlet_position_object_1.txt","r")

f.readline()
words = f.read().split()
for i in range(len(words)):
    words[i] = float(words[i])
xplanet = np.array(words[::2])
yplanet = np.array(words[1::2])

plt.plot(xplanet-xstar,yplanet-ystar)
#plt.plot(xstar,ystar)
plt.axis("equal")
plt.show()
