aprx = arcpy.mp.ArcGISProject("CURRENT")
maps = aprx.listMaps()
for map in maps:
    print ('--------------------------------------------------------------')
    print (map.name)
    print ('--------------------------------------------------------------')
    layers = map.listLayers()
    for layer in layers:
        if layer.supports('NAME') and layer.supports('LONGNAME') \
                    and layer.supports('DATASOURCE'):
            print (layer.longName + ' ---> ' + layer.dataSource)
