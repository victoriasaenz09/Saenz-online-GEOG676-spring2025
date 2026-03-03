import arcpy

#assign bands
source = r"D:\School\GEOG669\Saenz-online-GEOG676-spring2025\Lab7"
band1 = arcpy.sa.Raster(source + r"\blue.tif")
band2 = arcpy.sa.Raster(source + r"\green.tif")
band3 = arcpy.sa.Raster(source + r"\red.tif")
band4 = arcpy.sa.Raster(source + r"\nir08.tif")
combined = arcpy.CompositeBands_management([band1, band2, band3, band4], source + r"\output_combined.tif")

#HillShade
azimuth = 315
altitude = 45
shadows = 'NO_SHADOWS'
z_factor = 1
arcpy.ddd.HillShade(source + r"\dem_30m.tif", source + r"\output_hillshade.tif", azimuth, altitude, shadows, z_factor)

#Slope
output_measurement = 'DEGREE'
z_factor = 1
arcpy.ddd.Slope(source + r"\dem_30m.tif", source + r"\output_slope.tif", output_measurement, z_factor)

print("success!")