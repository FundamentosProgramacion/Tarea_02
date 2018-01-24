#Ricardo Cornejo Lozano A01746439
#calcula distancia entre 2 puntos con las cordenadas x1,y1,x2 y y2

x1 = int(input("teclea x1: "))
y1 = int(input("teclea y1: "))
x2 = int(input("teclea x2: "))
y2 = int(input("teclea y2: "))
distancia = (((x2-x1)**2) + ((y2-y1)**2))**0.5
print ("distancia:%.4f " % +distancia)
