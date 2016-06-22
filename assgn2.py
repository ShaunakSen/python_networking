import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url)
soup = BeautifulSoup(html)

tags = soup('span')

count = 0
sum = 0
for tag in tags:
    number = tag.contents[0]
    if number != '':
        number = int(number)
        count += 1
        sum += number

print "Count", count
print "Sum", sum
