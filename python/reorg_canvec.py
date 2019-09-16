import os
import arcpy
import logging

source_geodatabase = r"F:\CART3032\data\canvec\vancouver\canvec_190916_116785.gdb"

target_geodatabase_name = r"vancouver.gdb"
target_geodatabase_location = r"F:\CART3032\data\canvec\vancouver"
target_geodatabase = os.path.join(target_geodatabase_location, target_geodatabase_name)

coordinate_system = arcpy.SpatialReference("NAD 1983 UTM Zone 10N")

def init_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

def set_environment():
    arcpy.env.workspace = source_geodatabase
    arcpy.env.overwriteOutput = True

def create_geodatabase():
    arcpy.CreateFileGDB_management(target_geodatabase_location, target_geodatabase_name)
    logging.info("Geodatabase {} created.".format(target_geodatabase))

def get_name(feature_class):
    name = str(feature_class)
    return name.replace("_0", "_pt").replace("_1", "_ln").replace("_2", "_py")

def import_data():

    for feature_class in arcpy.ListFeatureClasses():

        row_count = arcpy.GetCount_management(feature_class)
        updated_name = get_name(feature_class)
        target_feature_class = os.path.join(target_geodatabase, updated_name)

        if (int(row_count[0]) > 0):
            logging.info("Processing feature {} ({})...".format(feature_class, row_count))
            arcpy.Project_management(feature_class, target_feature_class, coordinate_system)
        else:
            logging.info("Empty feature {} skipped.".format(feature_class))

def main():

    init_logging()

    try:
        set_environment()
        create_geodatabase()
        import_data()

    except arcpy.ExecuteError:
        logging.error(arcpy.GetMessage(2))

if __name__ == "__main__":
    main()