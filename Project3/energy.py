import numpy as np
import matplotlib.pyplot as plt

font = {"family":"sans serif","weight" : "normal", "size": 13}
plt.rc("font",**font)
plt.rcParams.update({'figure.autolayout': True})
T=10

for i in range(2):
    f = open("earthsunsystem/Euler_position_0_0001_object_"+str(i)+".txt")
    f.readline()
    words = np.array(f.read().split(),np.float)
    if i ==0:
        starxvalues = np.array(words[::2])
        staryvalues = np.array(words[1::2])
    else:
        planetxvalues = np.array(words[::2])
        planetyvalues = np.array(words[1::2])
    f.close()

for i in range(2):
    f = open("earthsunsystem/Euler_velocity_0_0001_object_"+str(i)+".txt")
    f.readline()
    words = np.array(f.read().split(),np.float)
    if i ==0:
        starvxvalues = np.array(words[::2])
        starvyvalues = np.array(words[1::2])
    else:
        planetvxvalues = np.array(words[::2])
        planetvyvalues = np.array(words[1::2])
    f.close()

relx = planetxvalues-starxvalues
rely = planetyvalues-staryvalues

relvx = planetvxvalues-starvxvalues
relvy = planetvyvalues-starvyvalues

kinetice = np.zeros(len(relx))
potentiale = np.zeros(len(relx))

m = 3.0024584*10**(-6)      #mass of the earth in solar mass

kinetice = 0.5*m*(relvx**2+relvy**2)
potentiale = -4*np.pi**2*m/np.sqrt(relx**2+rely**2)

totale = kinetice + potentiale

n = np.linspace(0,T,len(rely))

plt.plot(n,kinetice/np.amax(np.abs(kinetice)), label= "kinetic euler")
plt.title(r"Kinetisk energi for euler, $\Delta$t=0.0001 år")
plt.ylabel(r"$E_K \thinspace/\thinspace|E_{K,max}|$")
plt.xlabel("Tid [yr]")
plt.show()
plt.plot(n, potentiale/np.amax(np.abs(potentiale)), label ="potential euler")
plt.title(r"Potensiell energi for euler, $\Delta$t=0.0001 år")
plt.ylabel(r"$E_P \thinspace / \thinspace |E_{P,max}$|")
plt.xlabel("Tid [yr]")
plt.show()
plt.plot(n, totale/np.amax(np.abs(totale)), label = "total euler")
plt.title(r"Total energi for euler, $\Delta$t=0.0001 år")
plt.ylabel(r"$E_{Total} \thinspace / \thinspace |E_{Total,max}|$")
plt.xlabel("Tid [yr]")
plt.legend()
plt.show()

for i in range(2):
    f = open("earthsunsystem/verlet_position_0_0001_object_"+str(i)+".txt")
    f.readline()
    words = np.array(f.read().split(),np.float)
    if i ==0:
        vstarxvalues = np.array(words[::2])
        vstaryvalues = np.array(words[1::2])
    else:
        vplanetxvalues = np.array(words[::2])
        vplanetyvalues = np.array(words[1::2])
    f.close()

for i in range(2):
    f = open("earthsunsystem/verlet_velocity_0_0001_object_"+str(i)+".txt")
    f.readline()
    words = np.array(f.read().split(),np.float)
    if i ==0:
        vstarvxvalues = np.array(words[::2])
        vstarvyvalues = np.array(words[1::2])
    else:
        vplanetvxvalues = np.array(words[::2])
        vplanetvyvalues = np.array(words[1::2])
    f.close()

vrelx = vplanetxvalues-vstarxvalues
vrely = vplanetyvalues-vstaryvalues

vrelvx = vplanetvxvalues-vstarvxvalues
vrelvy = vplanetvyvalues-vstarvyvalues

kineticv = 0.5*m*(vrelvx**2+vrelvy**2)
potentialv = -4*np.pi**2*m/np.sqrt(vrelx**2+vrely**2)

totalv = kineticv + potentialv

nv = np.linspace(0,T,len(vrely))

plt.plot(nv,kineticv/np.amax(np.abs(kineticv)), label= "kinetic verlet")
plt.title(r"Kinetisk energi for velocity verlet, $\Delta$t=0.0001 år")
plt.ylim(0.99,1.01)
plt.ylabel(r"$E_K \thinspace/\thinspace|E_{K,max}$|")
plt.xlabel("Tid [yr]")
plt.show()
plt.plot(nv, potentialv/np.amax(np.abs(potentialv)), label ="potential verlet")
plt.title(r"Potensiell energi for velocity verlet, $\Delta$t=0.0001 år")
plt.ylim(-1.01,-0.99)
plt.ylabel(r"$E_P \thinspace / \thinspace |E_{P,max}|$")
plt.xlabel("Tid [yr]")
plt.show()
plt.plot(nv, totalv/np.amax(np.abs(totalv)), label = "total verlet")
plt.title(r"Total energi for velocity verlet, $\Delta$t=0.0001 år")
plt.ylim(-1.01,-0.99)
plt.ylabel(r"$E_{Total} \thinspace / \thinspace |E_{Total,max}|$")
plt.xlabel("tid [yr]")
plt.show()

plt.plot(n,totale/np.amax(np.abs(totale)), label= "euler")
plt.plot(nv,totalv/np.amax(np.abs(totale)),"k--", label ="verlet")
plt.title(r"Total energi for velocity verlet i mot euler,$\Delta$t = 0.0001 år")
plt.legend()
plt.ylabel(r"$E_{Total}/|E_{Total,max,Euler}$|")
plt.xlabel("Tid [yr]")
plt.show()
