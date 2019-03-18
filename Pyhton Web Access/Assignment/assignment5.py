import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter URL -')
#url = 'http://py4e-data.dr-chuck.net/comments_181132.xml'
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()

tree = ET.fromstring(data)
sum = 0
comments = tree.findall('comments/comment')
for comment in comments:
	#print('Name',comment.find('name').text)
	lst = comment.find('count').text
	lst.rstrip()
	sum = sum+int(lst)
	
print("Sum =",sum)		
