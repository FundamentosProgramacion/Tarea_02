#encoding: UTF-8

# Autor: Carlos Martínez Rodríguez
# Descripcion: El programa calcula la distancia entre dos puntos

# A partir de aquí escribe tu programa

cordenadaX1 = int(input("Coordenada x1: "))
cordenadaY1 = int(input("Coordenada y1: "))
cordenadaX2 = int(input("Coordenada x2: "))
cordenadaY2 = int(input("Coordenada y2: "))

distanciaEntrePuntos = (((cordenadaX2 - cordenadaX1) ** 2) + ((cordenadaY2 - cordenadaY1) **2)) ** 0.5

#Salidas
print("Distnacia entre dos puntos: %0.4f" % distanciaEntrePuntos)