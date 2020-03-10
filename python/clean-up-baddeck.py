#!c:/program files/arcgis/pro/bin/python/envs/arcgispro-py3/python.exe
# -*- coding: utf-8 -*-

import os
import arcpy
import logging

# root directory
root_directory = r"G:\Nautical"
# path to projection file
projection_file = os.path.join(root_directory, "Scripts", "BaddeckMercator.prj")
# path to geodatabase
geodatabase = os.path.join(root_directory, "Project", "Baddeck.gdb")
# source dataset
dataset = os.path.join(geodatabase, "S101")
# feature class and dataset postfix
feature_class_postfix = "_ClipPrj"
# study area
bbox = os.path.join(geodatabase, "BboxMainMap")

scratch_feature_class = os.path.join(geodatabase, "ScratchFeature")

arcpy.env.workspace = dataset
arcpy.env.overwriteOutput = True

spatial_reference = arcpy.SpatialReference(projection_file)

projected_dataset_name = "S101" + feature_class_postfix
projected_dataset = os.path.join(geodatabase, projected_dataset_name)


def init_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s  %(levelname)s %(message)s')


def clean_up():
    logging.info("Start clean-up...")
    # delete existing dataset
    arcpy.management.Delete(os.path.join(geodatabase, projected_dataset_name))
    # create a new dataset using projection file
    arcpy.management.CreateFeatureDataset(geodatabase, projected_dataset_name, spatial_reference)
    logging.info("Feature dataset {} created.".format(projected_dataset))

    feature_classes = arcpy.ListFeatureClasses()
    feature_classes_count = len(feature_classes)

    for index, feature_class in enumerate(feature_classes, 1):

        # count features within study area (bbox)
        features, _, count = arcpy.management.SelectLayerByLocation(feature_class, "intersect", bbox)
        target_feature_class = os.path.join(projected_dataset, feature_class + feature_class_postfix)

        if int(count) > 0:
            # clip features to study area, save as a temporary/scratch feature class
            arcpy.analysis.Clip(features, bbox, scratch_feature_class)
            # project clipped features
            arcpy.management.Project(scratch_feature_class, target_feature_class, spatial_reference)
            logging.info("{0:3d}/{1:3d} Feature class {2} projected and copied.".format(index, feature_classes_count, feature_class))

        else:
            logging.info("{0:3d}/{1:3d} Feature class {2} ignored. No records found.".format(index, feature_classes_count, feature_class))

    # delete temporary/scratch feature class
    arcpy.management.Delete(scratch_feature_class)
    logging.info("Scratch feature class deleted.")

    logging.info("Clean-up finished.")


def main():
    init_logging()
    clean_up()


if __name__ == "__main__":
    main()
