import urllib.request, urllib.parse, urllib.error
import json
url = input('Enter URL -')
uh = urllib.request.urlopen(url)

data = uh.read().decode()

info = json.loads(data)

lst = info["comments"]
sum = 0
count = 0
for x in lst:
	count = count+1
	sum = sum+int(x['count'])

print('Count =',count)
print('Sum =',sum)
