import urllib
import json

service_url = "http://python-data.dr-chuck.net/geojson?"

address = raw_input("Enter Location: ")
url = service_url + urllib.urlencode({'sensor': 'false', 'address': address})
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved..', len(data), 'Characters'
try:
    js = json.loads(str(data))
except:
    js = None

print data

if 'status' not in js or js['status'] != 'OK':
    print 'Failure to retrieve'
    print data


location = js['results'][0]['place_id']
print 'Place id:', location
