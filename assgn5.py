import urllib
import json

url = 'http://python-data.dr-chuck.net/comments_286488.json'

print 'Retrieving...', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved', len(data), 'characters'

js = json.loads(str(data))

comments = js['comments']

total = 0
number = 0
for comment in comments:
    count = int(comment['count'])
    number += 1
    total += count

print 'Count:', number
print 'Sum:', total
