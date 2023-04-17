from math import pow
#from math import round

with open('task_10_read.txt', 'r') as f1:
    lines = f1.readlines()

for line in lines:
    x = int(pow(int(line), 2))
    
    print(x)