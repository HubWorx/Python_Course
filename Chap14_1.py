import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_47819.xml'

uh = urllib.request.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)

total = 0
for counts in tree.iter('count'):
    total = total +int(counts.text)

print(total)

#counts = tree.findall('.//count')
#print(counts)



   # results = tree.findall('result')
    #lat = results[0].find('geometry').find('location').find('lat').text
    #lng = results[0].find('geometry').find('location').find('lng').text
    #location = results[0].find('formatted_address').text

    #print('lat', lat, 'lng', lng)
    #print(location)
