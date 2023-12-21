#дает информацию о определённом обьекте слоя

import osgeo.ogr 

shapfile = osgeo.ogr.Open(r"C:\Users\sticks\Desktop\My GIS\Vector Date\tl_2014_us_state\tl_2014_us_state.shp")
layer = shapfile.GetLayer(0)
feature = layer.GetFeature(12)
print("Геообьект №12 имеет следующие атрибуты:")
print("_______________________________________________________________________________________________")

attributes = feature.items()

for key, value in attributes.items():
    print("{} = {}".format(key, value))

geometry = feature.GetGeometryRef()
geometryName = geometry.GetGeometryName()

print("______________________________________________________________________________________________")\

print("Геотмерия заданного геообьекта представляет собой {}".format(geometryName))