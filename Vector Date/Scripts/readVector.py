from osgeo import ogr 

shapefile = ogr.Open("test/shapefile.shp")
layer = shapefile.GetLayer(0)

for i in range(layer.GetFeatureCount()):
    feauter = layer.GetFeature(i)
    id = feauter.GetField("ID")
    name = feauter.GetField("NAME")
    geometry = feauter.GetGeometryRef()
    print(i, name, geometry.GetX(), geometry.GetY())

shapefile = None

