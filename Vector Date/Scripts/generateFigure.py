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

for i in range(100):
    id = 1000 + i
    lat = random.uniform(-90,+90)
    long = random.uniform(-180,+180)
    name = str(id)+"_point-{}".format(long, lat)
    wkt = "POINT({} {})".format(long, lat)
    geometry = ogr.CreateGeometryFromWkt(wkt)
    feature = ogr.Feature(layer.GetLayerDefn())
    feature.SetGeometry(geometry) #задается геометрия обьекта
    feature.SetField("ID", id) #установить значения атрибутов слоя
    feature.SetField("NAME", name)
    layer.CreateFeature(feature)
    feature.Destroy()

datasource.Destroy()