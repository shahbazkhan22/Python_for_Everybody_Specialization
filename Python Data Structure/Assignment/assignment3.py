fname = 'mbox-short.txt'
fh = open(fname)
count = 0
num = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        num = num  + float(line[line.find(' '):])
        count = count+1
        
    #print(line)
print(num/count)