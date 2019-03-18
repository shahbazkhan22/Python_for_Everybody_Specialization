
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
def urlcalc(url,n,pos):
	if(n):
		# Ignore SSL certificate errors
		ctx = ssl.create_default_context()
		ctx.check_hostname = False
		ctx.verify_mode = ssl.CERT_NONE

		#url = input('Enter - ')
	
		html = urllib.request.urlopen(url, context=ctx).read()
		soup = BeautifulSoup(html, 'html.parser')

		# Retrieve all of the anchor tags
		tags = soup('a')
		x = 0
		for tag in tags:
			x = x+1
			url = (tag.get('href', None))
			if(x==pos):
				return(urlcalc(url,n-1,pos))
	else:
		return(url)
if __name__ == "__main__":
	url = input('Enter url --')
	#url = 'http://py4e-data.dr-chuck.net/known_by_Ngaire.html'
	count = int(input('Enter Count'))
	pos = int(input('Enter position'))
	print(urlcalc(url,count,pos))