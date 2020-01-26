# Iterates over all feature classes within a geodatabase, splits feature classes by feature code (ignores
# those without) and saves them in an output geodatabase. Later merges features classes based on 
# the dictionary.

# TODO cleanup code

import sys, os, shutil
import arcpy

enable_create_output_geodatabase = True
enable_merge_feature_classes = True

split_fields = ["FEAT_CODE"]

merge_dict = {
    "Highway_Ln" : ["RRRDHWW1", "RRRDHWX1", "RRRDHWY1"],
    "Highway_Bridge_Ln": ["RRBRHWY1", "RRBRHWX1"],
    "Arterial_Road_Ln": ["RRRDATY1", "RRRDLAY1"],
    "Arterial_Road_Bridge_Ln": ["RRBRATY1", "RRBRLAY1"],
    "Collector_Road_Ln": ["RRRDCOY1", "RRRDLCY1"],
    "Collector_Road_Bridge_Ln": ["RRRDCOY1"],
    "Local_Road_Ln": ["RRRDLOY1", "RRRDLOZ1"],
    "Local_Road_Bridge_Ln": ["RRBRLOY1", "RRBRLOZ1"],
    "Local_Road_Unpaved_Ln": ["RRRDLOY2", "RRRDLOZ2"],
    "Local_Road_Bridge_Unpaved_Ln": ["RRBRLOY2", "RRBRLOZ2"],
    "Local_Road_Tunnel_Paved_Ln": ["RRTULOZ1"],
    "Local_Road_Tunnel_Unpaved_Ln": ["RRTULOZ2"],
    "Local_Road_Dryweather_Ln": ["RRRDLODWZ2"],
    "Ramp_Ln": ["RRRDRPY1", "RRRDRPZ1"],
    "Ramp_Bridge_Ln": ["RRBRRPZ1"],
    "Ferry_Ln": ["RRRDDR50"],
    "Track_Ln": ["RRRDTK50"],
    "Track_Bridge_Ln": ["RRBRTK50"],
    "Track_Tunnel_Ln": ["RRTUTK50"],
    "Trail_Ln": ["RRRDTR50"],
    "Trail_Bridge_Ln": ["RRBRTR50"],
    "Forest_Py": ["LCTA40"],
    "Orchard_Py": ["LCOR40"],
    "Wharf_Py": ["WAWH40"],
    "Coast_River_Water_Py": ["WACORV40"],
    "Flume_Water_Py": ["WAFU40"],
    "Rapids_Py": ["WARA40"],
    "Dam_Py": ["WADM40"],
    "Lake_Py": ["WALK40"],
    "River_Water_Py": ["WALK40"],
    "River_Lake_Water_Py": ["WALK40"],
    "Reservoir_Water_Area_Py": ["WALK40"],
    "Canal_Water_Py": ["WALK40"],
    "Swamp_Py": ["WALK40"],
    "Coast_Water_Py": ["WALK40"],
    "Breakwater_Py": ["WALK40"],
    "Slipway_Py": ["WALK40"],
    "River_Ln": ["WARV50", "WARV55", "WARVSP50", "WARVSP55"],
    "Unterground_River_Ln": ["WARV56"],
    "Rapids_Ln": ["WARA50"],
    "Dam_Ln": ["WADM50"],
    "Coastline_Right_Ln": ["WACO20", "WACORV20", "WACOIS10"],
    "Coastline_Indefinite_Right_Ln": ["WACO25", "WACOIS15"],
    "Coastline_Lake_Left_Ln": ["WARV10", "WALKIS10"],
    "Coastline_Lake_Right_Ln": ["WALK20", "WARS20"],
    "Coastline_Lake_Indefinite_Right_Ln": ["WALK25"],
    "Coastline_River_Left_Ln": ["WARV10", "WARV15", "WACORVIS10"],
    "Coastline_River_Right_Ln": ["WARV20", "WARVIS10", "WARVLK20", "WARVLKIS10"],
    "Dyke_Right_Ln": ["WADYL0"],
    "Dyke_Left_Ln": ["WADYR0"],
    "Falls_Right_Ln": ["WAFAL0"],
    "Falls_Left_Ln": ["WAFAR0"]
}

file_path = r"C:\_data\geonova\20200115\Digby"

input_geodatabase = r"{}\digby.gdb".format(file_path)

output_geodatabase_file_name = "output.gdb"
output_geodatabase = r"{}\{}".format(file_path, output_geodatabase_file_name)

# arcpy.env.workspace = input_geodatabase

def create_output_geodatabase():
    print("Delete existing output geodatabase...")
    shutil.rmtree(output_geodatabase, ignore_errors=True)
    print("Create output geodatabase...")
    arcpy.management.CreateFileGDB(file_path, output_geodatabase_file_name)

    for path, _, feature_classes in arcpy.da.Walk(input_geodatabase, datatype="FeatureClass"):
        for feature_class in feature_classes:
            feature_class_path = os.path.join(path, feature_class)
            if split_fields[0] in [field.name for field in arcpy.ListFields(feature_class_path)]:
                print("Split feature class {}...".format(feature_class))
                arcpy.analysis.SplitByAttributes(feature_class_path, output_geodatabase, split_fields)

    # for feature_class in arcpy.ListFeatureClasses():
    #     if split_fields[0] in [field.name for field in arcpy.ListFields(feature_class)]:
    #         print("Split feature class {}...".format(feature_class))
    #         arcpy.analysis.SplitByAttributes(feature_class, output_geodatabase, split_fields)

def merge_feature_classes():
    for name, feature_codes in merge_dict.items():
        print("Merge {}...").format(feature_codes)
        feature_classes = [os.path.join(output_geodatabase, feature_code) for feature_code in feature_codes]
        output_feature_class = os.path.join(output_geodatabase, name)
        arcpy.management.Merge(feature_classes, output_feature_class)

if enable_create_output_geodatabase:
    create_output_geodatabase()

if enable_merge_feature_classes:
    merge_feature_classes()
