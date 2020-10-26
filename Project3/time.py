import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

font = {"family":"sans serif","weight" : "normal", "size": 13}
plt.rc("font",**font)
plt.rcParams.update({'figure.autolayout': True})

timee = np.zeros((4,5))
timev = np.zeros((4,5))



timee[0,:] = [0.260, 0.289, 0.285, 0.280, 0.286]
timev[0,:] = [0.542, 0.542, 0.598, 0.594, 0.599]

timee[1,:] = [2.688, 2.695, 2.712, 2.702, 2.691]
timev[1,:] = [5.846, 5.682, 5.844, 5.874, 5.689]

timee[2,:] = [23.926, 24.549, 23.299, 23.342, 24.323]
timev[2,:] = [50.915, 52.267, 50.432, 50.918, 50.996]

timee[3,:] = [224.673, 234.092, 437.804, 434.573, 435.540]
timev[3,:] = [506.473, 504.912, 974.899, 977.040, 975.879]





timeefinal = np.zeros(4)
timevfinal = np.zeros(4)

for i in range(len(timeefinal)):
    timeefinal[i] = np.sum(timee[i,:])/np.sqrt(len(timee[i,:]))
    timevfinal[i] = np.sum(timev[i,:])/np.sqrt(len(timev[i,:]))

h = np.array([0.00001,0.0001,0.001,0.01])

T = 10

N = np.sort(np.floor(T/h)+1)


plt.plot(np.log(N),np.log(timeefinal), label ="Euler")
plt.plot(np.log(N),np.log(timevfinal), label ="Velocity verlet")

plt.title("Tidssammenlikning")
plt.ylabel("log(Tid[ms]/1ms)")
plt.xlabel(" log(N)")
plt.legend()
plt.show()


valuese = stats.linregress(np.log(N),np.log(timeefinal))
valuesv = stats.linregress(np.log(N),np.log(timevfinal))

print("The time for euler goes like N^%.2f" %valuese[0])
print("The time for velocity verlet goes like N^%.2f" %valuesv[0]

error = np.zeros(4)

for i in range(len(timeefinal)):
    error[i] = (timevfinal[i]/timeefinal[i])*np.sqrt((np.std(timee[i,:])/np.sqrt(len(timee[i,:]))/timeefinal[i])**2+(np.std(timev[i,:])/np.sqrt(len(timev[i,:]))/timevfinal[i])**2)
    print("Velocity verlet takes %.2f +- %.2f times longer than euler when N is %g" %(timevfinal[i]/timeefinal[i],error[i],N[i]))
