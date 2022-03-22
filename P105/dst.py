import csv
import math
with open('data.csv') as f:
    csvreader = csv.reader(f)
    data = list(csvreader)
arr = data[0]
somme = 0
for h in arr:
    somme=somme+int(h)
mean= somme/len(arr)
dev = 0
for a in arr:
    dev = dev+((int(a)-mean)*(int(a)-mean))
num=dev/(len(arr)-1)
devitation = math.sqrt(num)
print(devitation)