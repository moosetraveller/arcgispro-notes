from qgis.core import QgsGeometry, QgsPoint

g = QgsGeometry.fromWkt('POINT ZM (1 2 5 60)') # your geometry

# if you don't need z and m, you could do this:

p = g.asPoint() # you'll get a QgsPointXY object
x = p.x()
y = p.y()

# if you need z and m, and you don't want to use regex, you could do this:

p = QgsPoint()
p.fromWkt(g.asWkt())

x = p.x()
y = p.y()
z = p.z()
m = p.m()

# example to parse multilinestring if you don't need z and m

g2 = QgsGeometry.fromWkt('MULTILINESTRING ((10 10, 20 20, 10 40),(40 40, 30 30, 40 20, 30 10))')
for points in g2.asMultiPolyline(): # asMultiPolyline() returns a list of a list of QgsPointXY
    point_list = [(p.x(), p.y()) for p in points] # converts QgsPointXY objects to a simple tuple
    print(point_list)
