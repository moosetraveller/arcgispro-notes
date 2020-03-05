#!c:/program files/arcgis/pro/bin/python/envs/arcgispro-py3/python.exe
# -*- coding: utf-8 -*-

import os
import arcpy
import logging

geodatabase = r"C:\Nautical\Project\Baddeck.gdb"
dataset = os.path.join(geodatabase, "S101")

arcpy.env.workspace = dataset
arcpy.env.overwriteOutput = True

spatial_reference = arcpy.SpatialReference(r"C:\Nautical\Scripts\BaddeckMercator.prj")

projected_dataset_name = "S101_Prj"
projected_dataset = os.path.join(geodatabase, projected_dataset_name)


def init_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s  %(levelname)s %(message)s')


def clean_up():
    logging.info("Start clean-up...")
    arcpy.management.CreateFeatureDataset(geodatabase, projected_dataset_name, spatial_reference)
    logging.info("Feature dataset {} created.".format(projected_dataset))

    for feature_class in arcpy.ListFeatureClasses():

        row_count = arcpy.management.GetCount(feature_class)
        target_feature_class = os.path.join(projected_dataset, feature_class + "_Prj")

        if int(row_count[0]) > 0:
            arcpy.management.Project(os.path.join(dataset, feature_class), target_feature_class, spatial_reference)
            logging.info("Feature class {} projected and copied.".format(feature_class))
        else:
            logging.info("Feature class {} ignored. No records found.".format(feature_class))

    logging.info("Clean-up finished.")


def main():
    init_logging()
    clean_up()


if __name__ == "__main__":
    main()
