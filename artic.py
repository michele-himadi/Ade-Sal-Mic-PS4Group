import urllib.request, urllib.parse, urllib.error
import json

artID = input('Enter the ID of the art: ')
serviceUrl = 'https://api.artic.edu/api/v1/artworks/' + artID

print('Retrieving', serviceUrl)
uh = urllib.request.urlopen(urllib.request.Request(serviceUrl, headers={'User-Agent' : 'Mozilla/5.0'}))
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None
    
for art in js:
    print("Title of art: ", art['title'])
