import osgeo.ogr

def findPoints(geometry, results):
    for i in range (geometry.GetPointCount()):
        x, y, z = geometry.GetPoint(i)
        if results['north'] == None or results['north'][1] < y:
            results['north'] = (x, y)
        if results['south'] == None or results['south'][1] > y:
            results['south'] = (x, y)

    for i in range (geometry.GetGeometryCount()):
        findPoints(geometry.GetGeometryRef(i), results)

shapefile = osgeo.ogr.Open(r"C:\Users\sticks\Desktop\My GIS\Vector Date\tl_2014_us_state\tl_2014_us_state.shp")
layer = shapefile.GetLayer(0)
feature = layer.GetFeature(13)
geometry = feature.GetGeometryRef()

results = {'north' : None,
           'south' : None}
findPoints(geometry,results)

print("Самая северная точка: ({:.4f}, {:.4f})".format(results['north'][0], results['north'][1])) 
print("Самая южная точка: ({:.4f}, {:.4f})". format( results['south'][0], results[ 'south'][1]))