import csv

f=open(r"Curve Fitting Script\data.csv",'w+')
fw=csv.writer(f)
t=int(input("Enter Number of Co-ordinates\n"))
paras=[]
for tt in range(t):
     print("Enter x and y Coordinates respectively\n")
     x,y = map(float,(input().split()))
     paras.append([x,y])
fw.writerows(paras)
f.close()
