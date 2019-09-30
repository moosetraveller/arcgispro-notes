#!c:/program files/arcgis/pro/bin/python/envs/arcgispro-py3/python.exe
# -*- coding: utf-8 -*-

# Read sources in current ArcGIS Pro project added to a map.
# - sorts sources by path
#
# Author: Thomas Zuberbuehler (thomas.zuberbuehler@gmail.com)

aprx = arcpy.mp.ArcGISProject("Current")
maps = aprx.listMaps()
for map in maps:
  layers = map.listLayers()
  sorted_layers = sorted(layers, key=lambda layer: layer.dataSource)
  for layer in sorted_layers:
    print (layer.dataSource)
