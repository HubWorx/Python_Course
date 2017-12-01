# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#Get user input
url = input('Enter - ')
count = int(input('Enter Count: '))
position = int(input('Enter Position: ')) - 1

#Set starting point of while loop
#url = "http://py4e-data.dr-chuck.net/known_by_Aamirah.html"
counts = 0
while counts < count:
# Retrieve all of the anchor tags
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    print("Retrieving: ",tags[position].get('href',None))
    url = tags[position].get('href',None)
    counts =  counts + 1
#for tag in tags:
    #print(tag.get('href', None))
