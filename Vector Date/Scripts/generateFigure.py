import os, os.path, shutil, random
from osgeo import ogr, osr 

if os.path.exists("test"):
    shutil.rmtree("test")

os.mkdir("test")

driver = ogr.GetDriverByName("ESRI Shapefile")
path = os.path.join("test", "shapefile.shp")

datasource = driver.CreateDataSource(path)

spatialReference = osr.SpatialReference()
spatialReference.SetWellKnownGeogCS( 'WGS84')

layer = datasource.CreateLayer("layer", spatialReference)


#блок ниже создаёт два поля в виле целого числа и строки, с заданной широтой и добавляет их в созданный ранее слой
field = ogr.FieldDefn("ID", ogr.OFTInteger) 
field.SetWidth (4)
layer.CreateField(field)
field = ogr.FieldDefn("NAME", ogr.OFTString)
field.SetWidth (20)
layer.CreateField(field)


print(help(os))
