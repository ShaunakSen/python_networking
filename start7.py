import urllib
import json

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = raw_input('Enter Location: ')
    if len(address) < 1:
        break
    url = serviceurl + urllib.urlencode({'sensor': 'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved...', len(data), 'characters'

    try:
        js = json.loads(str(data))
    except:
        js = None

    if 'status' not in js or js['status'] != 'OK':
        print 'Failure to retrieve'
        print data
        continue

    print data


    location = js['results'][0]['formatted_address']
    print 'Location:', location
    lat = js['results'][0]['geometry']['location']['lat']
    print "Latitude:", lat
    lng = js['results'][0]['geometry']['location']['lng']
    print "Longitude:", lng
