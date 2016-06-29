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


WEB SERVICES

they send data in - XML and JSON

main problem here is that java has hash maps. python has dictionaries
We need something that both of them can agree upon and then they convert
We call this the wire protocol

Python Dictionary ->(serialize)->Wire Format ->(de serialize)-> Java HashMap

serialize: int structure -> wire format
de serialize: reverse

it allows us to create sets of apps that work in diff languages
Wire Format -> XML and JSON
Note: in microsoft the trailing x ie .pptx means xml as they use xml to represent meta data


XML validator takes in an XML doc and a contract and decides if it is valid or not


Official dateTime formal
yyyy-mm-ddThh:mm:ssZ
Z->Time zone

This is bcoz in this format sorting is natural
ISRO 8601 format

Parsing XML in Python

We have some XML data

data = '''
<person>
    <name>Mini</name>
    <phone type="intl">
        8609131604
    </phone>
    <email hide="yes"/>
</person>
'''

This data is nothing but a String(Important)


Now we have a library xml.etree.ElementTree

import xml.etree.ElementTree as ET

we parse the string

tree = ET.fromstring(data)

this tree is an object
we can now run methods on this object to scrape out the underlying data
print 'Name:', tree.find('name').text
print 'Attr:', tree.find('email').get('hide')


JSON

import json

data = '''
{
  "name": "Mini",
  "phone": {
    "type": "intl"
    "number": "8609131604"
  },
  "email": {
    "hide": "yes"
  }
}
'''

info = json.loads(data)
loads => load from string
now this returns a PYTHON dictionary!! wow..

print info['name']
print info['phone']['type']


If we have data like:

data2 ='''
[
    {
        "id":"1",
        "x":"13",
        "name":"mini"
    },
    {
        "id":"2",
        "x":"13",
        "name":"shona"
    }
]
'''
info2 = json.loads(data2)

This returns a PYTHON list!

for item in info2:
    print item['id']
    print item['x']
    print item['name']



Service Oriented Approach

This is an approach by which an app can take data from various sources and bring them together


For eg when u book an airline ticket u can also book hotels!

So an app uses services from other apps
services often specify rules: this is url..we will give u json or xml

These web services are often called API
They have an application and we have an interface that can use the services the application provides.
So Application Program Interface


Web Service Technologies

SOAP and REST

SOAP - crappy and complicated

REST - Representational State Transfer(resource focused)

Remote resources which we CRUD remotely

OOP


class PatyAnimal:
    x = 0

    def party(self):
        self.x += 1
        print 'So far', self.x


mini = PatyAnimal()

mini.party()


mini.party() <=> PartyAnimal.party(mini)

this is how self becomes an alias of the object calling the method ie mini

Inheritance

class PartyAnimal2:
    x = 0
    name = ""

    def __init__(self, nam):
        self.name = nam
        print self.name, 'Constructed'

    def party(self):
        self.x += 1
        print self.name, "party count:", self.x


class FootballFan(PartyAnimal2):
    points = 0
    def touchdown(self):
        self.points += 7
        self.party()
        print self.name, "points:", self.points


FootballFan inherits everything in PartyAnimal2 .. vars, constructors , methods



Using Databases

Why do we use SQLite with python
MySql , oracle and all are rich db applications. They are quite heavy
SQLite is embedded db. this means it is built right in.
Our cars use SQLite, phones use it
It is in built in python


CREATE TABLE Users(
name VARCHAR(128),
email VARCHAR(128)
)

Why do we specify the max size?

understand that we store data in sql format so that retrieval is very fast from the disk
To maintain this speed it is essential that the size of data is known for fast lookup
if the size is 4M instead of 128 the data will be laid out differently

Also for security purpose we specify the size

Building a basic app


What we want to do is read the file mbox.txt and find all From: email  .. we want
to store the emails and the particular count of that email in a db

import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
curr = conn.cursor()

cursor is stored in the curr var

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')



name = raw_input('Enter file name:')
if len(fname) < 1:
    fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:

    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email, ))


Here we read from file and extract email

cur.execute('SELECT count FROM Counts WHERE email = ?', (email, ))

? is a placeholder

it is used to pass in arguments
here arguments is a tuple
(email, ) -> single tuple

The blank is reqd else python will confuse it as an expression

we could have done string concatenation also.. but we dont to avoid sql injection

cursor now has all the rows that meet that query

cur.execute('SELECT count FROM Counts WHERE email = ?', (email, ))
try:
    count = cur.fetchone()[0]
    cur.execute('UPDATE Counts SET count=count+1 WHERE email = ?', (email,))
except:
    cur.execute('''INSERT INTO Counts (email,count)
    VALUES (?,1)''', (email,))

conn.commit()

First we get count value for that email

cur.fetchone() fetches first row in form of a LIST
cur.fetchone()[0]
if it exists count = cur.fetchone()[0] would work
if it doesnt it wont be able to fetch so it will go to except block

Had we done cur.execute('SELECT * FROM Counts WHERE email = ?', (email,))

cur.fetchone() would hae been a list of 2 items : email and count

then count = cur.fetchone()[1]


conn.commit() -> write changes back to disk
put this outside the loop to make ur program run faster

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print str(row[0]), row[1]

cur.close()

row is also a list

Building a Data Model

Basic Rule: Dont put the same string twice. Use a relationship instead
in a column:

Mini
Mini

This is bad

make a table

1  Mini

And in second table put
1
1

Thus connection bw one table and another
This shortens string length
Here we had Mini
what if we had a 100 char string
we reference an int instead of that long string
That saves so much time

See the repitition of string problem in db_probs.png

The columns are

Track   Len     Artist      Album       Genre       Rating      Count


Go across all of the columns
See if that particular column represents a thing in the real world or is it an attribute of the thing?

Where to start?

Think about the thing ie most essential to the app
- Track

First table we are gonna build is the track table

Then look at all other columns?
Which of them are themselves tables and which are simply attributes of track?

Track
______
Title
Rating
Len
Count

This is our 1st table

Next Album

Track --->[belongs to]  Album --->[belongs to] Artist

Where does Genre fit in?

If genre was an attribute of album

Then changing genre of 1 song would change genre of all songs in album
Similarly for Artist

Track belongs to genre



Track                       Album
______                    __________

[id]                          [id]
title                         title
rating
len
count
(album_id)



album_id ------------->  id

it is a foreign key

Logical key is the title in both tables
It signifies that we use title for WHERE clauses ir for lookup
So we indicate to database that we will be searching by title often so store it in a manner
so that fast search is possible


Track                       Album               Artist
______                    __________          ___________

[id]                          [id]                 [id]
title                         title                name
rating                       (artist_id)
len
count
(album_id)

Album (artist_id) ---> Artist [id]

Track                       Album               Artist            Genre
______                    __________          ___________       ___________

[id]                          [id]                 [id]             [id]
title                         title                name             name
rating                       (artist_id)
len
count
(album_id)
(genre_id)

Track (genre_id) ----> Genre [id]

CREATE TABLE Track(id INTEGER NOT NULL
PRIMARY KEY AUTOINCREMENT UNIQUE,
 title TEXT, album_id INTEGER, genre_id INTEGER,
 len INTEGER, rating INTEGER, count INTEGER)

INSERT INTO Artist(name) VALUES('Led Zepplin')
INSERT INTO Genre(name) VALUES('Rock')

INSERT INTO Artist(name) VALUES('Led Zepplin')

Always build these tables outward in

ie construct track table at last

Finally if u look at all the data u have replication of nos but no replication of strings!!!

