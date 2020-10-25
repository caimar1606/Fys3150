import numpy as np
import matplotlib.pyplot as plt

font = {"family":"sans serif","weight" : "normal", "size": 13}
plt.rc("font",**font)
plt.rcParams.update({'figure.autolayout': True})


first = "betasystem/earth/verlet_position_"
last = "_object_"
dt = ["0_0001","0_0001_2_5","0_0001_2_9","0_0001_2_95","0_0001_2_99"]
beta = ["2","2,5","2,9","2,95","2,99"]
args = ["k","b--","y--","--","--"]
linew = ["2","1","1","1","1"]

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
    plt.plot(relx[i][:len(relx[i]//10):10],rely[i][:len(relx[i]//10):10],args[i], linewidth = linew[i], label = beta[i])


plt.title(r"Jordens bane over 10 år for forskjellige verdier av $\beta$")
plt.ylabel("y [AU]")
plt.xlabel("x [AU]")
plt.plot(0,0)
plt.legend()
plt.axis("equal")
plt.show()

first = "betasystem/ellipse/verlet_position_"
last = "_object_"
dt = ["0_0001_e_2_25","0_0001_e_2_5","0_0001_e_2_9","0_0001_e_2_99","0_0001_e"]
beta = ["2.25","2,5","2,9","2,99","2",]
args = ["r--","b--","y--","--","k"]
linew = ["1","1","1","1","1"]

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

relx = np.array(relx)
rely = np.array(rely)

for i in range(len(relx)):
    plt.plot(relx[i][:len(relx[i]//10):10],rely[i][:len(relx[i]//10):10],args[i], linewidth = linew[i], label = beta[i])


plt.title(r"Jordens bane over 10 år for forskjellige verdier av $\beta$")
plt.ylabel("y [AU]")
plt.xlabel("x [AU]")
plt.plot(0,0)
plt.legend()
plt.axis("equal")
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)
plt.show()
