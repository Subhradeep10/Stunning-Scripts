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