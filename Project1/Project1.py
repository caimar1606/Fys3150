#editors note: if you want to run with n=10**7, then you must uncomment all commented codelines
#and run the cpp program for i=7. The reason for this is that the output files go over githubs
#max file size.

import numpy as np
import matplotlib.pyplot as plt


fastnames = ["runs/run1/timefast","runs/run2/timefast","runs/run3/timefast","runs/run4/timefast","runs/run5/timefast","runs/run6/timefast","runs/run7/timefast"]
slownames = ["runs/run1/timeslow","runs/run2/timeslow","runs/run3/timeslow","runs/run4/timeslow","runs/run5/timeslow","runs/run6/timeslow","runs/run7/timeslow"]

fast = []
slow = []
for names in fastnames:
    f = open(names,"r")
    file = f.read()
    words = file.split()
    words = words[4:]
    for i in range(len(words)):
        words[i]=float(words[i])
    fast.append(words[1::2])
for names in slownames:
    f = open(names,"r")
    file = f.read()
    words = file.split()
    words = words[4:]
    for i in range(len(words)):
        words[i]=float(words[i])
    slow.append(words[1::2])
    f.close()

slowavg = []
fastavg = []
slowstd = []
faststd = []

for i in range(len(slow[0])):
    sums = 0
    sumf = 0
    stdsums = 0
    stdsumf = 0

    for j in range(len(slow)):
        sums += slow[j][i]
        sumf += fast[j][i]
    slowavg.append(sums/len(slow))
    fastavg.append(sumf/len(slow))
    for j in range(len(slow)):
        stdsums += abs(slow[j][i]-sums/len(slow))**2
        stdsumf += abs(fast[j][i]-sumf/len(fast))**2
    slowstd.append(np.sqrt(stdsums/len(slow)))
    faststd.append(np.sqrt(stdsumf/len(fast)))


arrslowavg = np.array(slowavg)
arrfastavg = np.array(fastavg)
arrslowstd = np.array(slowstd)
arrfaststd = np.array(faststd)

for i in range(len(arrslowavg)):
    print("The slow algorithm takes on average %.4f ms  +- %.4f ms when n = %g"%(arrslowavg[i]*1000,arrslowstd[i]*1000,10**(i+1)))
    print("The fast algorithm takes on average %.4f ms +- %.4f ms when n = %g"%(arrfastavg[i]*1000,arrfaststd[i]*1000,10**(i+1)))


multavg = arrslowavg/arrfastavg
multavgstd = multavg*np.sqrt((arrslowstd/arrslowavg)**2+(arrfaststd/arrfastavg)**2)
for i in range(1,len(slow)+1):
    print("The slow algorithm takes %.1f +- %.1f times longer than the fast algorithm when n = %g." %(multavg[i-1],multavgstd[i-1],10**i))
print(" ")
print("The slow algorithm takes %.1f +- %.1f times longer on average"%(multavg.mean(),np.std(multavg)))

datanames1 = ["runs/run1/output1fast","runs/run2/output1fast","runs/run3/output1fast","runs/run4/output1fast","runs/run5/output1fast","runs/run6/output1fast","runs/run7/output1fast"]
datanames2 = ["runs/run1/output2fast","runs/run2/output2fast","runs/run3/output2fast","runs/run4/output2fast","runs/run5/output2fast","runs/run6/output2fast","runs/run7/output2fast"]
datanames3 = ["runs/run1/output3fast","runs/run2/output3fast","runs/run3/output3fast","runs/run4/output3fast","runs/run5/output3fast","runs/run6/output3fast","runs/run7/output3fast"]
datanames4 = ["runs/run1/output4fast","runs/run2/output4fast","runs/run3/output4fast","runs/run4/output4fast","runs/run5/output4fast","runs/run6/output4fast","runs/run7/output4fast"]
datanames5 = ["runs/run1/output5fast","runs/run2/output5fast","runs/run3/output5fast","runs/run4/output5fast","runs/run5/output5fast","runs/run6/output5fast","runs/run7/output5fast"]
datanames6 = ["runs/run1/output6fast","runs/run2/output6fast","runs/run3/output6fast","runs/run4/output6fast","runs/run5/output6fast","runs/run6/output6fast","runs/run7/output6fast"]
#datanames7 = ["runs/run1/output7fast","runs/run2/output7fast","runs/run3/output7fast","runs/run4/output7fast","runs/run5/output7fast","runs/run6/output7fast","runs/run7/output7fast"]

error1=[]
error2=[]
error3=[]
error4=[]
error5=[]
error6=[]
#error7=[]

for names in datanames1:
    f = open(names,"r")
    file = f.read()
    words = file.split()
    words = words[5:]
    for i in range(len(words)):
        words[i]=float(words[i])
    error1.append(words[3::4])
    if names == "runs/run1/output1fast":
        approx1 = words[1::4]
        x1 = words[0::4]
    f.close()

for names in datanames2:
    f = open(names,"r")
    file = f.read()
    words = file.split()
    words = words[5:]
    for i in range(len(words)):
        words[i]=float(words[i])
    error2.append(words[3::4])
    if names == "runs/run1/output2fast":
        approx2 = words[1::4]
        x2 = words[0::4]
    f.close()

for names in datanames3:
    f = open(names,"r")
    file = f.read()
    words = file.split()
    words = words[5:]
    for i in range(len(words)):
        words[i]=float(words[i])
    error3.append(words[3::4])
    if names == "runs/run1/output3fast":
        approx3 = words[1::4]
        x3 = words[0::4]
        exact = words[2::4]
    f.close()

for names in datanames4:
    f = open(names,"r")
    file = f.read()
    words = file.split()
    words = words[5:]
    for i in range(len(words)):
        words[i]=float(words[i])
    error4.append(words[3::4])
    f.close()


for names in datanames5:
    f = open(names,"r")
    file = f.read()
    words = file.split()
    words = words[5:]
    for i in range(len(words)):
        words[i]=float(words[i])
    error5.append(words[3::4])
    f.close()


for names in datanames6:
    f = open(names,"r")
    file = f.read()
    words = file.split()
    words = words[5:]
    for i in range(len(words)):
        words[i]=float(words[i])
    error6.append(words[3::4])
    f.close()
"""
for names in datanames7:
    f = open(names,"r")
    file = f.read()
    words = file.split()
    words = words[5:]
    for i in range(len(words)):
        words[i]=float(words[i])
    error7.append(words[3::4])
    f.close()
"""

plt.plot(x1,approx1, label = "n=10")
plt.plot(x2,approx2, label = "n=100")
plt.plot(x3,approx3, label = "n=1000")
plt.plot(x3,exact, label = "exact")

plt.legend()
plt.title("Plott for approximasjonen for forskjellige n-verdier")
plt.xlabel("x")
plt.ylabel("u(x)")
plt.show()

maxerrors = []

for j in range(len(error1)):
    maxerror = [0,0,0,0,0,0] #add 1 more 0 if using n = 10**7 files
    for i in range(2,len(error1[0])): #we skip the first element since that one always is NaN
        if abs(error1[j][i]) > maxerror[0]:
            maxerror[0] = abs(error1[j][i])
        if abs(error2[j][i]) > maxerror[1]:
            maxerror[1] = abs(error2[j][i])
        if abs(error3[j][i]) > maxerror[2]:
            maxerror[2] = abs(error3[j][i])
        if abs(error4[j][i]) > maxerror[3]:
            maxerror[3] = abs(error4[j][i])
        if abs(error5[j][i]) > maxerror[4]:
            maxerror[4] = abs(error5[j][i])
        if abs(error6[j][i]) > maxerror[5]:
            maxerror[5] = abs(error6[j][i])
        #if abs(error7[j][i]) > maxerror[6]:
        #    maxerror[6] = abs(error7[j][i])
    maxerrors.append(maxerror)
print(maxerrors)

meanerrorsum1 = 0
meanerrorsum2 = 0
meanerrorsum3 = 0
meanerrorsum4 = 0
meanerrorsum5 = 0
meanerrorsum6 = 0
#meanerrorsum7 = 0


for i in range(len(maxerrors)):
    meanerrorsum1 += maxerrors[i][0]
    meanerrorsum2 += maxerrors[i][1]
    meanerrorsum3 += maxerrors[i][2]
    meanerrorsum4 += maxerrors[i][3]
    meanerrorsum5 += maxerrors[i][4]
    meanerrorsum6 += maxerrors[i][5]
    #meanerrorsum7 += maxerrors[i][6]

meanerror1 = meanerrorsum1/len(maxerrors)
meanerror2 = meanerrorsum2/len(maxerrors)
meanerror3 = meanerrorsum3/len(maxerrors)
meanerror4 = meanerrorsum4/len(maxerrors)
meanerror5 = meanerrorsum5/len(maxerrors)
meanerror6 = meanerrorsum6/len(maxerrors)
#meanerror7 = meanerrorsum7/len(maxerrors)


print("Log10 of the mean maximum error when n = 10 is %g" %(np.log10(abs(meanerror1))))
print("Log10 of the mean maximum error when n = 100 is %g" %(np.log10(abs(meanerror2))))
print("Log10 of the mean maximum error when n = 1000 is %g" %(np.log10(abs(meanerror3))))
print("Log10 of the mean maximum error when n = 10000 is %g" %(np.log10(abs(meanerror4))))
print("Log10 of the mean maximum error when n = 100000 is %g" %(np.log10(abs(meanerror5))))
print("Log10 of the mean maximum error when n = 1000000 is %g" %(np.log10(abs(meanerror6))))
#print("Log10 of the mean maximum error when n = 10000000 is %g" %(np.log10(abs(meanerror7))))
