import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_286484.xml'

data = urllib.urlopen(url).read()

stuff = ET.fromstring(data)
comments = stuff.findall('comments/comment')
total = 0
print 'Count:', len(comments)

for comment in comments:
    count = comment.find('count').text
    count = int(count)
    total += count


print 'Sum:', total
