geoDatabaseName = 'ADD NAME OF GEODATABASE OR THE ROOT PATH TO THE DATASOURCE HERE'

aprx = arcpy.mp.ArcGISProject("CURRENT")
maps = aprx.listMaps()
for map in maps:
    print ('--------------------------------------------------------------')
    print (map.name)
    print ('--------------------------------------------------------------')
    layers = map.listLayers()
    check = 'OK'
    for layer in layers:
        if layer.supports('DATASOURCE') and not(geoDatabaseName in layer.dataSource):
            if layer.supports('NAME') and layer.supports('LONGNAME'):
                print (layer.longName + ' ---> ' + layer.dataSource)
            check = 'NOK'
    print (check)
