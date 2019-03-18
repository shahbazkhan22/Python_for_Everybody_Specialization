fname = 'words.txt'
fh = open(fname)
for line in fh:
    #line.strip()
    print(line.strip().upper())