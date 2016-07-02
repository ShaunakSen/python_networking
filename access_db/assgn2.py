import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb2.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
)''')

cur.execute('''
CREATE TABLE IF NOT EXISTS Genre(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
)''')

cur.execute('''
CREATE TABLE IF NOT EXISTS Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
)''')

cur.execute('''
CREATE TABLE IF NOT EXISTS Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
)''')

fname = 'tracks/Library.xml'


def lookup(d, key):
    found = False
    for child in d:
        if found:
            return child.text
        if child.text == key and child.tag == 'key':
            found = True
    return None


stuff = ET.parse(fname)

all = stuff.findall('dict/dict/dict')

print 'Dict count:', len(all)

for entry in all:
    if lookup(entry, 'Track ID') is None:
        continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    genre = lookup(entry, 'Genre')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or album is None or artist is None or genre is None:
        continue

    print name, genre, artist, album, count, rating, length

    cur.execute('''
    INSERT OR IGNORE INTO Artist(name)
    VALUES ( ? )
    ''', (artist, ))

    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''
    INSERT OR IGNORE INTO Album (title, artist_id)
    VALUES ( ?, ? )
    ''', (album, artist_id))

    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''
    INSERT OR IGNORE INTO Genre(name)
    VALUES ( ? )
    ''', (genre, ))

    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''
    INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count)
    VALUES ( ?, ?, ?, ?, ?, ? )
    ''', (name, album_id, genre_id, length, rating, count))

    conn.commit()