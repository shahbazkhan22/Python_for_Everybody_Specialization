from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
#url = 'http://py4e-data.dr-chuck.net/comments_181130.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
sum = 0
for tag in tags:
	t = str(tag)
	num = re.findall('([0-9]+)',t)
	for n in num:
		sum = sum+int(n)
    
print(sum)