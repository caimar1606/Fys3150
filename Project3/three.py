import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

font = {"family":"sans serif","weight" : "normal", "size": 13}
plt.rc("font",**font)
plt.rcParams.update({'figure.autolayout': True})

names = ["Jorda", "Jupiter"]

first = "threebody/verlet_position_"
last = "_object_"
dt = ["0_0001"]

relx = []
rely = []

for t in range(len(dt)):
    for i in range(3):
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

relx1 = np.array(relx)
rely1 = np.array(rely)

for i in range(len(relx1)):
    plt.plot(relx1[i],rely1[i],label = names[i])

plt.title(r"Trelegeme for 100 år med $\Delta$t = 0.0001 år")
plt.ylabel("y [AU]")
plt.xlabel("x [AU]")
plt.plot(0,0,"b*")
plt.legend()
plt.axis("equal")
plt.show()



dt = ["0_00001_10"]

relx = []
rely = []

for t in range(len(dt)):
    for i in range(3):
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
    plt.plot(relx[i],rely[i],label = names[i])

plt.title(r"Trelegemeover 100 år med $\Delta$t = 0.00001 år og 10$\cdot M_J$")
plt.ylabel("y [AU]")
plt.xlabel("x [AU]")
plt.legend()
plt.plot(0,0,"b*")
plt.axis("equal")
plt.show()

for i in range(len(relx)):
    plt.plot(relx[i],rely[i],label = '%s system 2' %(names[i]))
    plt.plot(relx1[i],rely1[i],label = names[i])

plt.title(r"Sammenligning av trelegeme over 100 år med $\Delta_t$ = 0.00001 år")
plt.ylabel("y [AU]")
plt.xlabel("x [AU]")
plt.legend()
plt.plot(0,0,"b*")
plt.axis("equal")
plt.show()

dt = ["0_00001_1000"]

relx = []
rely = []

for t in range(len(dt)):
    for i in range(3):
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
    plt.plot(relx[i],rely[i],label = names[i])

plt.title(r"Trelegeme over 100 år med $\Delta$t = 0.00001 år og 1000$\cdot M_J$")
plt.ylabel("y [AU]")
plt.xlabel("x [AU]")
plt.legend()
plt.plot(0,0,"b*")
plt.xlim(-4,5)
plt.ylim(-6,3)
plt.show()
