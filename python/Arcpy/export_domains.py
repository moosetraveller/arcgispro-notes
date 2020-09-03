#!c:/program files/arcgis/pro/bin/python/envs/arcgispro-py3/python.exe
# -*- coding: utf-8 -*-

# Exports given domains from a CanVec geodatabase to DBF files and
# updates the description field (removes everything except the
# English description)
#
# Author: Thomas Zuberbuehler (thomas.zuberbuehler@gmail.com)

import os
import arcpy
from arcpy.sa import *

arcpy.env.overwriteOutput = True

geodatabase_name = r"Vancouver.gdb"
geodatabase_location = r"G:\CART3032\projects\Vancouver"
geodatabase = os.path.join(geodatabase_location, geodatabase_name)

target_location = r"C:\Temp"

code_field = "Key"
value_field = "Value"

domains = [
    "road_class_cl",
    "building_function_cl",
]
# domains = arcpy.Describe(geodatabase).domains

for domain in domains:
    dbf = os.path.join(target_location, domain + ".dbf")
    arcpy.DomainToTable_management(geodatabase, str(domain), dbf, code_field, value_field)
    with arcpy.da.UpdateCursor(dbf, [value_field]) as cursor:
        for row in cursor:
            row[0] = row[0].split(": ")[1].split(" / ")[0]
            cursor.updateRow(row)
