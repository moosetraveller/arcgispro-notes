import re

point = "POINT ZM (1 2 5 60)"

m = re.match("POINT ZM [(](?P<X>\d+) (?P<Y>\d+) (?P<Z>\d+) (?P<M>\d+)[)]", point)

x = m.group('X')
y = m.group('Y')
z = m.group('Z')
m = m.group('M')

print(x, y, z, m)
