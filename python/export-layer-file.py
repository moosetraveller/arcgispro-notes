#!c:/program files/arcgis/pro/bin/python/envs/arcgispro-py3/python.exe
# -*- coding: utf-8 -*-

import os
import glob
import arcpy
import logging

root_directory = r"G:\Nautical"
# aprx_file_path = os.path.join(root_directory, "Examples", "Project 2", "Project 2.aprx")
aprx_file_path = "CURRENT"
style_file_directory = os.path.join(root_directory, "Project", "Styles")
map_name = "Maritime"

# initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s  %(levelname)s %(message)s')

# open ArcGIS Pro project
aprx = arcpy.mp.ArcGISProject(aprx_file_path)
# get map
map = aprx.listMaps(map_name)[0]

for layer in map.listLayers():
    if not layer.isGroupLayer:
        layer_file_path = os.path.join(style_file_directory, layer.name)
        arcpy.management.SaveToLayerFile(layer, layer_file_path, is_relative_path="RELATIVE")
        logging.info("Style file {}.lyrx exported.".format(layer_file_path))

logging.info("All style files exported.")
