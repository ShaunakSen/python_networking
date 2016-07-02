import xml.etree.ElementTree as ET
import sqlite3

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
    lookup(entry, 'Name')
