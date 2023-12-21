#пример создания и записи растровых данных
#испортируем все нужные библиотеки или их комоненты
from osgeo import gdal
from osgeo import osr 
import random
import struct


driver = gdal.GetDriverByName("GTIFF") #получить формат данных по короткому имени. Не уверен, что это именно формат, кажется что-то типа настроек формата данных (расширения?)
dstrFile = driver.Create("Образец растра.tiff", 360, 180, 1, ) #создание файла в формате tiff с 360 колонкамми 180 столбцами, с 1 каналом

stapiapReference = osr.SpatialReference() #позволяет выбрать необходимую проекцию и систему координат
stapiapReference.SetWellKnownGeogCS("WGS84") #выбор этой самой системы координат
dstrFile.SetProjection(stapiapReference.ExportToWkt()) #назначаем выбранную проекцию нашему созданному файлу

#задаем область интереса
originX = -180
originY = 90
cellWidth = 1.0
cellHieght = 1.0
dstrFile.SetGeoTransform([originX, cellWidth, 0, #формируем из отдельных областей интереса список
                           originY, 0, -cellHieght])

band = dstrFile.GetRasterBand(1) #получаем инфомрацию из растра о первом канале

values = [] #создаем пустую переменную под значения

for row in range(180): #заполняем пустой список значениями для создания растра с необходимыми свойствами
    row_date = []
    for col in range(360):
        row_date.append(random.randint(1, 100))
    values.append(row_date)


fmt = "<" + ("h" * band.XSize)  #позволяет записывать построчно на диск данные о растре
for row in range(180):
    scanline = struct.pack(fmt, *values[row]) #Эта строка создает формат для структуры данных, используемой для записи данных в растровый блок. "<" - это конец строки, "h" - это формат для 16-битного целого числа, "*" - это оператор умножения, который повторяет строку "h" band.XSize раз.
    band.WriteRaster(0, row, 360, 1, scanline)
