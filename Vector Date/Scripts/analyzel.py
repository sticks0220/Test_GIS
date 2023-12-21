#выдаёт основную информацию о слое(пространственную привязку, число обьектов, число слоев)

import osgeo.ogr
shapefile = osgeo.ogr.Open(r"C:\Users\sticks\Desktop\My GIS\Vector Date\tl_2014_us_state\tl_2014_us_state.shp") #задаётся путь к шейп файлу 
numLayers = shapefile.GetLayerCount() #метод GetLayerCount выводит количество слоёв в шейпе
print("Шейп содержит {} слоев".format(numLayers))
print("______________________________________________________________________________________________________________")

for layerNum in range(numLayers):
    layer = shapefile.GetLayer(layerNum)
    spatialRef = layer.GetSpatialRef().ExportToProj4()
    numFeatures = layer.GetFeatureCount()
    print("Слой {} имеет пространственную привязку {}".format(
        layerNum, spatialRef))
    print ("Слой {} содержит {} геообъектов: " . format( 
        layerNum, numFeatures)) 
    print ("______________________________________________________________________________________________________________")
    for featureNum in range(numFeatures): 
        feature = layer.GetFeature(featureNum) 
        featureName = feature.GetField("NAME")
        print ("Геообъект {} под названием {}". 
format(featureNum, featureName))