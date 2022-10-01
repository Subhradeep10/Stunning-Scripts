import os 

path = input('Enter the path to the files: ')

metricsList = (
    'creation date',
    'modification date',
    'title', 
    'size'
)

for count, i in enumerate(metricsList, start=1):
    print(f'{count}. {i}')

metricsChoice = int(input("Enter the number corresponding to the metric: "))
commonName = input('\nEnter the common name for the files: ')

filePaths = []

for i in os.listdir(path):
    filePaths.append(path + i)

if metricsChoice == 1:
    filePaths.sort(key = os.path.getctime)
elif metricsChoice == 2:
    filePaths.sort(key=os.path.getmtime)
elif metricsChoice == 3:
    filePaths.sort()
elif metricsChoice == 4:
    filePaths.sort(key=os.path.getsize)

n = 1
for src in filePaths:
    ext = src.split('.')[-1]
    os.rename(src, f'{path}/{commonName} {n}.{ext}')
    n += 1