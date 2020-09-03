# Script prepares GeoNova dataset for an export to Adobe Illustrator with ArcMap.
#
# Iterates over all feature classes within a geodatabase, splits feature classes
# by feature code (ignores those without) and saves them in an output
# geodatabase. Later merges features classes based on the dictionary.

import sys, os, shutil
import arcpy

split_fields = ["FEAT_CODE"]

file_path = r"C:\_data\geonova\20200115\Digby"

input_geodatabase = os.path.join(file_path, "digby.gdb")

intermediate_geodatabase_file_name = "intermediate.gdb"
intermediate_geodatabase = os.path.join(file_path, intermediate_geodatabase_file_name)

output_geodatabase_file_name = "output.gdb"
output_geodatabase = os.path.join(file_path, output_geodatabase_file_name)

# projection = arcpy.SpatialReference(2961)

merge_dict = {
    "Highway_Ln" : ["RRRDHWW1", "RRRDHWX1", "RRRDHWY1"],
    "Highway_Bridge_Ln": ["RRBRHWY1", "RRBRHWX1"],
    "Arterial_Road_Ln": ["RRRDATY1", "RRRDLAY1"],
    "Arterial_Road_Bridge_Ln": ["RRBRATY1", "RRBRLAY1"],
    "Collector_Road_Ln": ["RRRDCOY1", "RRRDLCY1"],
    "Collector_Road_Bridge_Ln": ["RRBRCOY1"],
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
    "River_Water_Py": ["WARV40"],
    "River_Lake_Water_Py": ["WARVLK40"],
    "Reservoir_Water_Area_Py": ["WARS40"],
    "Canal_Water_Py": ["WACA40"],
    "Swamp_Py": ["WASW40"],
    "Coast_Water_Py": ["WACO40"],
    "Breakwater_Py": ["WABW40"],
    "Slipway_Py": ["WASP40"],
    "River_Ln": ["WARV50", "WARV55", "WARVSP50", "WARVSP55"],
    "Unterground_River_Ln": ["WARV56"],
    "Rapids_Ln": ["WARA50"],
    "Dam_Ln": ["WADM50"],
    "Coastline_Right_Ln": ["WACO20", "WACORV20", "WACOIS10"],
    "Coastline_Indefinite_Right_Ln": ["WACO25", "WACOIS15"],
    "Coastline_Lake_Left_Ln": ["WALKIS10"],
    "Coastline_Lake_Right_Ln": ["WALK20", "WARS20"],
    "Coastline_Lake_Indefinite_Right_Ln": ["WALK25"],
    "Coastline_River_Left_Ln": ["WARV10", "WARV15", "WACORVIS10"],
    "Coastline_River_Right_Ln": ["WARV20", "WARVIS10", "WARVLK20", "WARVLKIS10"],
    "Dyke_Right_Ln": ["WADYL0"],
    "Dyke_Left_Ln": ["WADYR0"],
    "Falls_Right_Ln": ["WAFAL0"],
    "Falls_Left_Ln": ["WAFAR0"],
    "Building_Pt": ["BLCC60", "BLDG60", "BLDG63", "BLFA60", "BLSH60", "BLTH60", "STWM60"],
    "Church_Pt": ["BLCH60"],
    "FireStation_Pt": ["BLFS60"],
    "Greenhouse_Pt": ["BLGH60"],
    "Library_Pt": ["BLLI60"],
    "Museum_Pt": ["BLMU60"],
    "PostOffice_Pt": ["BLPO60"],
    "PoliceStation_Pt": ["BLPS60"],
    "GasStation_Pt": ["BLPU60"],
    "LandmarkTree_Pt": ["LCTS60"],
    "Gate_Pt": ["STGT60", "STGT65"],
    "Lighthouse_Pt": ["STLH60"],
    "Silo_Pt": ["STSO60"],
    "Tank_Pt": ["UTTK60"],
    "Tower_Pt": ["UTTO60", "UTTO65"],
    "Falls_Pt": ["WAFA60"],
    "Rapids_Pt": ["WARA60"],
    "Rock_Pt": ["WARK60"],
    "County_Boundary_Ln": ["DLBNCO50"],
    "Municipality_Boundary_Ln": ["DLBNMU50"],
    "Historic_Site_Ln": ["DLHS50", "DLHSNA50"],
    "Indian_Reserve_Ln": ["DLIR50"],
    "Military_Reserve_Ln": ["DLMR50"],
    "Protected_Area_Ln": ["DLPA50"],
    "National_Park_Ln": ["DLPKNA50"],
    "Cliff_Left_Ln": ["LFCFL0"],
    "Cliff_Right_Ln": ["LFCFR0"],
    "Contour_Index_Ln": ["LFCI50", "LFCI55"],
    "Contour_Regular_Ln": ["LFCO50", "LFCO55"],
    "Depression_Left_Ln": ["LFDCL0", "LFDCL5"],
    "Depression_Right_Ln": ["LFDCR0", "LFDCR5"],
    "Depression_Index_Left_Ln": ["LFDIL0"],
    "Depression_Index_Right_Ln": ["LFDIR0", "LFDIR5"],
    "Embankement_Ln": ["LFEM50"],
    "Pipeline_AboveGround_Ln": ["UTPI50"],
    "Transmission_Ln": ["UTTR50"],
    "Building_Py": ["BLAR40", "BLCC40", "BLDG40", "BLDG43", "BLFA40", "BLSC40", "BLSH40", "BLTH40"],
    "Church_Py": ["BLCH40"],
    "FireStation_Py": ["BLFS40"],
    "Fort_Py": ["BLFT40"],
    "Greenhouse_Py": ["BLGH40"],
    "Hospital_Py": ["BLHO40"],
    "PostOffice_Py": ["BLPO40"],
    "PoliceStation_Py": ["BLPS40"],
    "County_Boundary_Py": ["DLBNCO40"],
    "Municipality_Boundary_Py": ["DLBNMU40"],
    "Historic_Site_Py": ["DLHS40", "DLHSNA40"],
    "Indian_Reserve_Py": ["DLIR40"],
    "Military_Reserve_Py": ["DLMR40"],
    "Protected_Area_Py": ["DLPA40"],
    "National_Park_Py": ["DLPKNA40"],
    "Provincial_Park_Py": ["DLPKPR40"],
    "Bridge_Py": ["RRBR40"],
    "Footbridge_Py": ["RRFB40"],
    "Overpass_Py": ["RROP40"],
    "Pool_Py": ["STPO40"],
    "Utility_Py": ["UTSP40", "UTSS40", "UTTK40"]
}

def create_geodatabases():
    print("Delete existing output geodatabase...")
    shutil.rmtree(intermediate_geodatabase, ignore_errors=True)
    shutil.rmtree(output_geodatabase, ignore_errors=True)
    print("Create geodatabases...")
    arcpy.management.CreateFileGDB(file_path, intermediate_geodatabase_file_name)
    arcpy.management.CreateFileGDB(file_path, output_geodatabase_file_name)

def split_by_attribute():
    for path, _, feature_classes in arcpy.da.Walk(input_geodatabase, datatype="FeatureClass"):
        for feature_class in feature_classes:
            feature_class_path = os.path.join(path, feature_class)
            if split_fields[0] in [field.name for field in arcpy.ListFields(feature_class_path)]:
                print("Split feature class {}...".format(feature_class))
                arcpy.analysis.SplitByAttributes(feature_class_path, intermediate_geodatabase, split_fields)

def merge_feature_classes():
    for name, feature_codes in merge_dict.items():
        print("Merge {} to {}...").format(feature_codes, name)
        feature_classes = [os.path.join(intermediate_geodatabase, feature_code) for feature_code in feature_codes]
        output_feature_class = os.path.join(output_geodatabase, name)
        arcpy.management.Merge(feature_classes, output_feature_class)

def clean_up():
    print("Delete existing intermediate geodatabase...")
    shutil.rmtree(intermediate_geodatabase, ignore_errors=True)

def main():
    create_geodatabases()
    split_by_attribute()
    merge_feature_classes()
    clean_up()

if __name__== "__main__":
  main()
