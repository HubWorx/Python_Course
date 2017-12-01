import json
import urllib.request, urllib.parse, urllib.error

#url = input("Enter Location:")
url = "http://py4e-data.dr-chuck.net/comments_47820.json"
print("Retrieving:", url)

uh=urllib.request.urlopen(url)
data=uh.read().decode()

info = json.loads(data)

#print(json.dumps(info, indent=4))

count = 0
for items in info["comments"]:
    count = count + (int(items["count"]))
print(count)
