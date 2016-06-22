import urllib
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/known_by_Jian.html'

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('a')

tag = tags[17]
requiredLink = tag.get('href', None)
print tag.contents[0]

for i in range(6):
    html = urllib.urlopen(requiredLink).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    tag = tags[17]
    requiredLink = tag.get('href',None)
    print tag.contents[0]
