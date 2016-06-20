import urllib
from BeautifulSoup import *

url = raw_input("Enter - ")

html = urllib.urlopen(url).read()
print html

soup = BeautifulSoup(html)

tags = soup('a')
print tags

for tag in tags:
    print tag.get('href', None)
