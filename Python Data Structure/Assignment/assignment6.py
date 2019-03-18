file = open('mbox-short.txt')
dict = {}
words = []
maxCount = 0
maxMail = None
for line in file:
    if line.startswith('From') and not line.startswith('From:'):
        words.append(line.split()[1])
for word in words:
    dict[word] = dict.get(word,0) + 1
for mail,count in dict.items():
    if(count>maxCount):
        maxCount = count
        maxMail = mail
print(maxMail,maxCount)
