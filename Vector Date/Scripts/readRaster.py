from osgeo import gdal
import numpy

srcFile = gdal.Open("Образец растра.tiff") #открываем для чтения файл
band = srcFile.GetRasterBand(1) #запрашиваем информацию о канале под номером 1 из нашего растра

#import struct не работает, ругается на размер буфера. numpy же читает растр спокойно
#fmt = "<" + ("h" * band.XSize) # длина строки канала  = 180
#for row in range (band.YSize):
   # scanline = band.ReadRaster(0, row, band.XSize, 1,
                     #          band.XSize, 1,
                     #          band.DataType)
   # row_data = struct.unpack(fmt, scanline)
   # print(row_data)
 
values = band.ReadAsArray() #читает как массив
for row in range(band.XSize - 180): # отсчет с нуля, выводит все значения начиная с нуля по строкам
    print(values[row])
