fname = 'romeo.txt'
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    lst.sort()
    if not line in lst:
    	lst = lst + (line.split())
lst.sort()
newLst = []
for i in range(len(lst)-1):
    if(lst[i]!=lst[i+1]):
        newLst.append(lst[i])
newLst.append(lst[len(lst)-1])
print(newLst)
