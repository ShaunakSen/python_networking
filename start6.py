import json

data = '''
{
  "name": "Mini",
  "phone": {
    "type": "intl",
    "number": "8609131604"
  },
  "email": {
    "hide": "yes"
  }
}
'''

info = json.loads(data)
print info['name']
print info['phone']['type']


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
print len(info2)
for item in info2:
    print item['id']
    print item['x']
    print item['name']
