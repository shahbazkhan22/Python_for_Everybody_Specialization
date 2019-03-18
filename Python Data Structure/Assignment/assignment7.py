file = open('mbox-short.txt')
words = []
dict = {}
for line in file:
    if line.startswith('From') and not line.startswith('From:'):
        words.append(line.split()[5].split(':')[0])
words.sort()
for word in words:
    dict[word] = dict.get(word,0)+1
for time,count in dict.items():
    print(time,count)