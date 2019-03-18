import re
file = open('ActualData.txt')
number = []
sum = 0
for line in file:
    line = line.rstrip()
    num = re.findall('([0-9]+)',line)
    for n in num:
        sum = sum+int(n)
print(sum)