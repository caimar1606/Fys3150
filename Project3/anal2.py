import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

font = {"family":"sans serif","weight" : "normal", "size": 13}
plt.rc("font",**font)
plt.rcParams.update({'figure.autolayout': True})

efirst = "earthsunsystem/Euler_position_"
elast = "_object_"

nr = 1

dt = ["0_01","0_001","0_0001","0_00001"]
dtval = np.array([0.01,0.001,0.0001,0.00001])
T=10

errors= np.zeros((nr,len(dt)))


for t in range(len(dt)):
    for i in range(2):
        f = open(efirst+dt[t]+elast+str(i)+".txt")
        f.readline()
        words = np.array(f.read().split(),np.float)
        if i ==0:
            starxvalues = np.array(words[::2])
            staryvalues = np.array(words[1::2])
        else:
            planetxvalues = np.array(words[::2])
            planetyvalues = np.array(words[1::2])
            error = 1 - np.sqrt((planetxvalues-starxvalues)**2+(planetyvalues-staryvalues)**2)
            errors[i-1,t] = np.amax(np.abs(error))
            plt.plot(planetxvalues-starxvalues,planetyvalues-staryvalues, label = "Planet %g" %(i))
        f.close()
    plt.title(r"Orbit for one planet: Euler with $\Delta$t = %g" %(dtval[t]))
    plt.axis("equal")
    plt.xlabel("x[AU]")
    plt.ylabel("y[AU]")
    plt.legend()
    plt.show()

h = dtval


for j in range(nr):
    for i in range(len(errors[0,:])):
        print("The maximum error for the Euler method for planet %g is %f when dt is %g years" %(j+1,errors[j,i],dtval[i]))

plt.plot(np.log(h), np.log(errors[0,:]))
plt.ylabel("log(Relative error)")
plt.xlabel("log(h)")
plt.show()

vals = stats.linregress(np.log(h),np.log(errors[0,:]))

print("The error of the Euler method goes like h^%.2f"%(vals[0]))

vfirst = "earthsunsystem/verlet_position_"
errorsv = np.zeros((nr,len(dt)))


for t in range(len(dt)):
    for i in range(2):
        f = open(vfirst+dt[t]+elast+str(i)+".txt")
        f.readline()
        words = np.array(f.read().split(),np.float)
        if i ==0:
            starxvalues = np.array(words[::2])
            staryvalues = np.array(words[1::2])
        else:
            planetxvalues = np.array(words[::2])
            planetyvalues = np.array(words[1::2])
            error = 1 - np.sqrt((planetxvalues-starxvalues)**2+(planetyvalues-staryvalues)**2)
            errorsv[i-1,t] = np.amax(np.abs(error))
            plt.plot(planetxvalues-starxvalues,planetyvalues-staryvalues, label = "Planet %g" %(i))
        f.close()
    plt.title(r"Orbit for one planet: Velocity verlet with dt = %g years" %(dtval[t]))
    plt.axis("equal")
    plt.xlabel("x[AU]")
    plt.ylabel("y[AU]")
    plt.legend()
    plt.show()

for j in range(nr):
    for i in range(len(errorsv[0,:])):
        print("The maximum error for the velocity verlet method for planet %g is %f when dt is %g" %(j+1,errorsv[j,i],dtval[i]))

plt.plot(np.log(h) , np.log(errorsv[0,:]))
plt.ylabel("log(Relative error)")
plt.xlabel("log(h)")
plt.show()

slope = (np.log(errorsv[0,1])-np.log(errorsv[0,0]))/(np.log(h[1])-np.log(h[0]))

print("The error for the Velocity Verlet goes like h^%.2f"%slope)
