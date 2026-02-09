# creating a gdb and the garage features.
import arcpy 

arcpy.env.workspace = r'D:\School\GEOG669\Saenz-online-GEOG676-spring2025\Lab4\codes_env'
folder_path = r'D:\School\GEOG669\Saenz-online-GEOG676-spring2025\Lab4'
gdb_name = 'Test.gdb'
gdb_path = folder_path + '\\' + gdb_name
arcpy.CreateFileGDB_management(folder_path, gdb_name)

csv_path = r'D:\School\GEOG669\Saenz-online-GEOG676-spring2025\Lab4\garages.csv'
garage_layer_name = 'Garage_Points'
garages = arcpy.MakeXYEventLayer_management(csv_path, 'X', 'Y', garage_layer_name)

input_layer = garages
arcpy.FeatureClassToGeodatabase_conversion(input_layer, gdb_path)
garage_points = gdb_path + '\\' + garage_layer_name

# open the campus gdb and copy building feature to our gdb
campus = r'D:\School\GEOG669\Saenz-online-GEOG676-spring2025\Lab4\campus.gdb'
buildings_campus = campus + '\\' + '\Structures'
buildings = gdb_path + '\\' + 'Buildings'

arcpy.CopyFeatures_management(buildings_campus, buildings)

# Re-projection
spatial_ref = arcpy.Describe(buildings).spatialReference
arcpy.Project_management(garage_points, gdb_path + '\Garage_Points_reprojected', spatial_ref)

#Buffering the garages
garageBuffered = arcpy.Buffer_analysis(gdb_path + '\Garage_Points_reprojected', gdb_path + '\Garage_Points_buffered', 150)

# Intersecting the buffers with the buildings
arcpy.Intersect_analysis([garageBuffered, buildings], gdb_path + '\Garage_Building_Intersect', 'ALL')

arcpy.TableToTable_conversion(gdb_path + '\Garage_Building_Intersect.dbf', 'D:\School\GEOG669\Saenz-online-GEOG676-spring2025\Lab4', 'nearbyBuildings.csv')