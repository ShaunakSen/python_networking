import _sqlite3

conn = _sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

cur.execute('SELECT id FROM Course WHERE title = ? ', ('si106', ))

temp = cur.fetchone()
print temp