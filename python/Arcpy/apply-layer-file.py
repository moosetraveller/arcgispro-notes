#!c:/program files/arcgis/pro/bin/python/envs/arcgispro-py3/python.exe
# -*- coding: utf-8 -*-

import os
import glob
import arcpy
import logging

root_directory = r"G:\Nautical"
# aprx_file_path = os.path.join(root_directory, "Project", "Baddeck.aprx")
aprx_file_path = "CURRENT"
style_file_directory = os.path.join(root_directory, "Project", "Styles")
map_name = "Baddeck Chart"
# feature class and dataset postfix
feature_class_postfix = "_Prj"

# initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s  %(levelname)s %(message)s')

# open ArcGIS Pro project
aprx = arcpy.mp.ArcGISProject(aprx_file_path)
# get map
map = aprx.listMaps(map_name)[0]

# get all layer files in style file directory
layer_files = glob.glob(os.path.join(style_file_directory, "*.lyrx"))
# extract layer names from layer files
layer_names = [layer_file[layer_file.rindex(os.sep)+1:-5] for layer_file in layer_files]
# update names according to dictionary
layer_names = [name + feature_class_postfix for name in layer_names]

# create dictionary with layer name
layer_file_dictionary = dict(zip(layer_names, layer_files))

for layer in map.listLayers():
    if layer.name in layer_names:
        arcpy.management.ApplySymbologyFromLayer(layer, layer_file_dictionary.get(layer.name), update_symbology="MAINTAIN")
        logging.info("Style file applied to {}.".format(layer.longName))

logging.info("All style files applied.")
