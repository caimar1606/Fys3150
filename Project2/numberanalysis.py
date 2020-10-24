import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as lin

n = np.array([10,50,75,100,150,200]) #size of matrix

count = np.array([165,4598,10481,18743,42048,75009])

plt.plot(n,count, "bo-")
plt.title("Plott for antall iterasjoner")
plt.xlabel("n")
plt.ylabel("Iterasjoner")
plt.xlim(np.min(n)-10,np.max(n)+10)
plt.ylim(np.min(count)-5000,np.max(count)+5000)
plt.show()

for i in range(len(n)):
    count[i]=count[i]/n[i]

slope,intercept,r_value,p_value,std_err = lin.linregress(n,count)
print("The constant of the function is %.3f +- %.3f"%(slope,std_err))

plt.plot(n,count,"ko-")
plt.title("Plott for antall interasjoner delt med n")
plt.xlabel("n")
plt.ylabel("Iterasjoner/n")
plt.xlim(np.min(n)-10,np.max(n)+10)
plt.ylim(np.min(count)-10,np.max(count)+10)
plt.show()
