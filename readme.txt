import urllib
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

for line in fhand:
    print line.strip()


Urllib allows to read from url like files

counts = dict()

for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print counts


We are basically doing what?
in web browser we issue a GET req. browser serves us html. we click on a link to
issue another request.....
Here we are doing same stuff but with python program
so we have captchas and all to distinguish between the 2