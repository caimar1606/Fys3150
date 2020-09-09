import numpy as np

#This code just analyzes the times we got from LU-decomposition

names = ["runs/runLU/data1","runs/runLU/data2","runs/runLU/data3","runs/runLU/data4"]

data = []

for file in names:
    f = open(file,"r")
    line = f.read()
    words = line.split()
    words = words[3:]
    for i in range(len(words)):
        words[i] = float(words[i])
    data.append(words)

arr1 = np.array(data[0])
arr2 = np.array(data[1])
arr3 = np.array(data[2])
arr4 = np.array(data[3])


print("The average time when n = 10**1 is %.2f +- %.2f "%(np.mean(arr1),np.std(arr1)))
print("The average time when n = 10**2 is %.2f +- %.2f "%(np.mean(arr2),np.std(arr2)))
print("The average time when n = 10**3 is %.1f +- %.1f "%(np.mean(arr3),np.std(arr3)))
print("The average time when n = 10**4 is %.0f +- %.0f "%(np.mean(arr4),np.std(arr4)))
