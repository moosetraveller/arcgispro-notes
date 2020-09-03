#!c:/program files/arcgis/pro/bin/python/envs/arcgispro-py3/python.exe
# -*- coding: utf-8 -*-

# Reorganizes and reprojects CanVec data.
# - Creates a new Geodatabase (overwrites an existing one)
# - Creates a dataset 'canvec'
# - Projects feature classes with at least 1 feature and saves them in the new geodatabase
# - Renames feature classes (_0 -> _pt, _1 -> _ln, _2 -> _py)
# - Updates alias for each feature class (removes underscores and use title case)
#
# Author: Thomas Zuberbuehler (thomas.zuberbuehler@gmail.com)

import os
import arcpy
import logging

source_geodatabase = r"G:\CART3032\data\canvec\vancouver\canvec_190916_116785.gdb"

target_geodatabase_name = r"Vancouver.gdb"
target_geodatabase_location = r"G:\CART3032\projects\Vancouver"
target_geodatabase = os.path.join(target_geodatabase_location, target_geodatabase_name)

target_feature_dataset = "canvec"

coordinate_system = arcpy.SpatialReference("NAD 1983 UTM Zone 10N")

def init_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s  %(levelname)s %(message)s')

def set_environment():
    arcpy.env.workspace = source_geodatabase
    arcpy.env.overwriteOutput = True

def create_geodatabase():
    arcpy.CreateFileGDB_management(target_geodatabase_location, target_geodatabase_name)
    logging.info("Geodatabase {} created.".format(target_geodatabase))

def create_feature_dataset():
    arcpy.CreateFeatureDataset_management(target_geodatabase, target_feature_dataset, coordinate_system)

def get_updated_name(feature_class):
    return str(feature_class).replace("_0", "_pt").replace("_1", "_ln").replace("_2", "_py")

def get_alias(feature_class_name):
    return feature_class_name.replace("_", " ").title()

def reorganize_data():

    create_feature_dataset()

    for feature_class in arcpy.ListFeatureClasses():

        row_count = arcpy.GetCount_management(feature_class)
        updated_name = get_updated_name(feature_class)
        target_feature_class = os.path.join(target_geodatabase, target_feature_dataset, updated_name)

        if (int(row_count[0]) > 0):
            logging.info("Processing feature class {} ({})...".format(feature_class, row_count))
            arcpy.Project_management(feature_class, target_feature_class, coordinate_system)
            arcpy.AlterAliasName(target_feature_class, get_alias(updated_name))
        else:
            logging.info("Empty feature class {} ignored.".format(feature_class))

def main():

    init_logging()

    try:
        set_environment()
        create_geodatabase()
        reorganize_data()

    except arcpy.ExecuteError:
        logging.error(arcpy.GetMessage(2))

if __name__ == "__main__":
    main()
