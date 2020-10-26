import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

font = {"family":"sans serif","weight" : "normal", "size": 13}
plt.rc("font",**font)
plt.rcParams.update({'figure.autolayout': True})

nr=1
T = 100

first = "mercurysunsystem/verlet_position_"
last = "_object_"
dt = "0_000001_nonrel"
dtval = 0.000001

for i in range(2):
    f = open(first+dt+last+str(i)+".txt")
    f.readline()
    words = np.array(f.read().split(),np.float)
    if i ==0:
        starxvalues = np.array(words[::2])
        staryvalues = np.array(words[1::2])
    else:
        planetxvalues = np.array(words[::2])
        planetyvalues = np.array(words[1::2])
        error = np.sqrt((planetxvalues-starxvalues)**2+(planetyvalues-staryvalues)**2)
        errors = np.amax(np.abs(error))
    f.close()

relx = planetxvalues-starxvalues
rely = planetyvalues-staryvalues

t = np.linspace(0,T,len(relx))


plt.plot(relx,rely, label = "Mercury")
plt.plot(0,0,"b*")
plt.title(r"Orbit for Mercury with dt = %g years" %(dtval))
plt.axis("equal")
plt.xlabel("x[AU]")
plt.ylabel("y[AU]")
plt.legend()
plt.show()


r = np.sqrt(relx**2+rely**2)

peri=[0]
i = 1
while i <= len(relx)-2:
    if r[i+1]-r[i] > 0 and r[i]-r[i-1] <0:
        peri.append(i)
        i+=10
    i+=1
peri = np.array(peri)

tan = rely[peri]/relx[peri]

angle = np.degrees(np.arctan(tan))

plt.plot(t[peri],angle)

vals = stats.linregress(t[peri],angle)


plt.plot(t,t*vals[0]+vals[1])
plt.title('Lineærregresjon for Perihelionvinkelen ')
plt.xlabel('Tid [yr]')
plt.ylabel(r'Grader [$^o$]' )
plt.show()

print(r'Endringen over et århundre er %.4f grader ' %(vals[0]*T))
