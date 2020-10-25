import numpy as np
import matplotlib.pyplot as plt

font = {"family":"sans serif","weight" : "normal", "size": 13}
plt.rc("font",**font)
plt.rcParams.update({'figure.autolayout': True})

first = "escapevelocity/verlet_position_"
last = "_object_"
dt = ["0_0001_8_6","0_0001_8_7","0_0001_8_8","0_0001_8_9","0_001_exact"]
velocity = ["8.6 [AU/YR]","8.7 [AU/YR]","8.8 [AU/YR]","8.9 [AU/YR]",r"2$\pi\sqrt{2}$ [AU/YR]"]

relx = []
rely = []

for t in range(len(dt)):
    for i in range(2):
        f = open(first+dt[t]+last+str(i)+".txt")
        f.readline()
        words = np.array(f.read().split(),np.float)
        if i ==0:
            starxvalues = np.array(words[::2])
            staryvalues = np.array(words[1::2])
        else:
            planetxvalues = np.array(words[::2])
            planetyvalues = np.array(words[1::2])
        f.close()

    relx.append(planetxvalues-starxvalues)
    rely.append(planetyvalues-staryvalues)


for i in range(len(relx)):
    plt.plot(relx[i],rely[i], label = velocity[i])

plt.title(r"Escapevelocity over 10år med $\Delta$t = 0.0001 år")
plt.ylabel("y [AU]")
plt.xlabel("x [AU]")

plt.plot(0,0,"b*")
plt.legend()
plt.ylim(-20,30)
plt.xlim(-100,20)
plt.show()
