import numpy as np
import matplotlib.pyplot as plt

names = ["runs/L20/T1/L20T1Vec0","runs/L20/T1/L20T1Vec4","runs/L20/T1/L20T1Vec5"]
names2 = ["runs/L20/T2_4/L20T2_4Vec0","runs/L20/T2_4/L20T2_4Vec4","runs/L20/T2_4/L20T2_4Vec5"]

name = [r'$\langle E \rangle$', r'$\langle |M| \rangle$', 'N flips']

for i in range(len(names)):
    f = open(names[i])

    words = f.read().split()[1:]

    vec = [float(j) for j in words]

    if i == 2:
        newvec = np.zeros(len(vec))
        for j in range(1001):
            newvec[j] = np.sum(vec[:j+1])
        vec = newvec

    mcc = np.linspace(1,len(vec),len(vec))

    plt.title(r' %s mot antall Monte Carlo sykluser (MCC), ved T=1 og L=20' %(name[i]))
    plt.xlabel('MCC', fontsize=15)
    plt.ylabel(name[i], fontsize=15)
    plt.plot(mcc[:1000],vec[:1000])
    plt.show()


for i in range(len(names2)):
    f = open(names2[i])

    words = f.read().split()[1:]

    vec = [float(j) for j in words]

    mcc = np.linspace(1,len(vec),len(vec))

    if i == 2:
        newvec = np.zeros(len(vec))
        for j in range(1001):
            newvec[j] = np.sum(vec[:j+1])
        vec = newvec

    plt.title(r' %s mot antall Monte Carlo sykluser (MCC), ved T=2.4 og L=20' %(name[i]))
    plt.xlabel('MCC', fontsize=15)
    plt.ylabel(name[i], fontsize=15)
    plt.plot(mcc[:1000],vec[:1000])
    plt.show()


names = ["runs/L20/T1/L20T1UPVec0","runs/L20/T1/L20T1UPVec4","runs/L20/T1/L20T1UPVec5"]
names2 = ["runs/L20/T2_4/L20T2_4UPVec0","runs/L20/T2_4/L20T2_4UPVec4","runs/L20/T2_4/L20T2_4UPVec5"]


for i in range(len(names)):
    f = open(names[i])

    words = f.read().split()[1:]

    vec= [float(j) for j in words]

    if i == 2:
        newvec = np.zeros(len(vec))
        for j in range(1001):
            newvec[j] = np.sum(vec[:j+1])
        vec = newvec

    mcc = np.linspace(1,len(vec),len(vec))

    plt.title(r' %s mot antall Monte Carlo sykluser (MCC), ved T=1, L=20, der spinn = 1' %(name[i]))
    plt.xlabel('MCC', fontsize=15)
    plt.ylabel(name[i], fontsize=15)
    plt.plot(mcc[:1000],vec[:1000])
    plt.show()


for i in range(len(names2)):
    f = open(names2[i])

    words = f.read().split()[1:]

    vec= [float(j) for j in words]

    if i == 2:
        newvec = np.zeros(len(vec))
        for j in range(1001):
            newvec[j] = np.sum(vec[:j+1])
        vec = newvec

    mcc = np.linspace(1,len(vec),len(vec))

    plt.title(r' %s mot antall Monte Carlo sykluser (MCC), ved T=2.4, L=20, der spinn=1' %(name[i]))
    plt.xlabel('MCC', fontsize=15)
    plt.ylabel(name[i], fontsize=15)
    plt.plot(mcc[:1000],vec[:1000])
    plt.show()

enames = ["runs/L20/T1/L20T1Vec6","runs/L20/T2_4/L20T2_4Vec6"]
limit = [0.1,0.7]
temp = [1, 2.4]
j=0
for i in range(len(enames)):
    f = open(enames[i])

    words = f.read().split()[1:]

    vec= [float(k) for k in words[10000:]]

    average = np.average(vec)

    mcc = np.linspace(1,len(vec),len(vec))


    min = average-limit[j]
    max = average+limit[j]

    plt.title(r' Fordelingen av energier E, ved T=%.1f, L=20' %(temp[i]))
    plt.xlabel('E', fontsize=15)
    plt.ylabel('N', fontsize=15)

    plt.hist(vec,bins = 17,range=(min,max),color ="c")
    plt.axvline(average, color='g', linestyle='dashed', linewidth=3)
    plt.show()
    j+=1
