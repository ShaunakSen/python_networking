import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x="2">
            <id>123</id>
            <name>Mini</name>
        </user>
        <user x="1">
            <id>11323</id>
            <name>Shona</name>
        </user>
    </users>
</stuff>
'''

stuff = ET.fromstring(input)
users = stuff.findall('users/user')
for user in users:
    name = user.find('name').text
    valueX = user.get('x')
    id = user.find('id').text
    print name
    print valueX
    print id
