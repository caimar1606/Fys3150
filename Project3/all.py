import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

font = {"family":"sans serif","weight" : "normal", "size": 13}
plt.rc("font",**font)
plt.rcParams.update({'figure.autolayout': True})


first = "allplanets/verlet_position_"
last = "_object_"
dt = ["0_00001"]
names = ["Merkur", "Venus", "Jorda", "Mars", "Jupiter","Saturn", "Uranus", "Neptun"]

relx = []
rely = []

for t in range(len(dt)):
    for i in range(9):
        f = open(first+dt[t]+last+str(i)+".txt")
        f.readline()
        words = np.array(f.read().split(),np.float)
        if i ==0:
            starxvalues = np.array(words[::2])
            staryvalues = np.array(words[1::2])
        else:
            planetxvalues = np.array(words[::2])
            planetyvalues = np.array(words[1::2])
            relx.append(planetxvalues-starxvalues)
            rely.append(planetyvalues-staryvalues)
        f.close()

relx = np.array(relx)
rely = np.array(rely)

for i in range(len(relx)):
    plt.plot(relx[i][::10],rely[i][::10], label = names[i])

plt.title(r"Solsystemet for 100 år med $\Delta$t = 0.00001 år")
plt.ylabel("y [AU]")
plt.xlabel("x [AU]")
plt.legend()
plt.plot(0,0,"b*")
plt.axis("equal")
plt.show()

first = "allplanets/verlet_position_"
last = "_object_"
dt = ["0_0001"]
names = ["Merkur", "Venus", "Jorda", "Mars", "Jupiter","Saturn", "Uranus", "Neptun"]

relx = []
rely = []

for t in range(len(dt)):
    for i in range(9):
        f = open(first+dt[t]+last+str(i)+".txt")
        f.readline()
        words = np.array(f.read().split(),np.float)
        if i ==0:
            starxvalues = np.array(words[::2])
            staryvalues = np.array(words[1::2])
        else:
            planetxvalues = np.array(words[::2])
            planetyvalues = np.array(words[1::2])
            relx.append(planetxvalues-starxvalues)
            rely.append(planetyvalues-staryvalues)
        f.close()

relx = np.array(relx)
rely = np.array(rely)

for i in range(len(relx)):
    plt.plot(relx[i][::20],rely[i][::20], label = names[i])

plt.title(r"Solsystemet for 1000 år med $\Delta$t = 0.0001 år")
plt.ylabel("y [AU]")
plt.xlabel("x [AU]")
plt.legend()
plt.plot(0,0,"b*")
plt.axis("equal")
plt.show()
