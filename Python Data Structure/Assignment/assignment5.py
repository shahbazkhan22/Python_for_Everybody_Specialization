file = open('mbox-short.txt')
count = 0
lst = []
for line in file:
    if line.startswith('From') and not line.startswith('From:'):
        #lst = line.split()
        print(line.rstrip().split()[1])
        count = count+1
print('There were',count,'lines in the file with From as the first word')