import osgeo.ogr

def analyzelGeometry(geometry, indent = 0):
    s = []
    s.append(" " * indent)
    s.append(geometry.GetGeometryName())
    if geometry.GetPointCount() > 0:
        s.append(" с {} точками данных".format(geometry.GetPointCount()))
    if geometry.GetGeometryCount() > 0:
        s.append(" содержит: ")
     
    print("".join(s))

    for i in range (geometry.GetGeometryCount()):
        analyzelGeometry(geometry.GetGeometryRef(i), indent+1)
    
shapfile = osgeo.ogr.Open(r"C:\Users\sticks\Desktop\My GIS\Vector Date\tl_2014_us_state\tl_2014_us_state.shp")
layer = shapfile.GetLayer(0)
feauter = layer.GetFeature(12)
geometry = feauter.GetGeometryRef()

analyzelGeometry(geometry)