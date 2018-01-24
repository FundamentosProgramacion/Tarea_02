#encoding: UTF-8

# Autor: Andrés Reyes Rangel
# Descripción: Calcular la distancia entre dos puntos.

x1= int(input("primer coordenada en x: "))
y1= int(input("primer coordenada en y: "))
x2= int(input("segunda coordenada en x: "))
y2= int(input("segunda coordenada en y: "))

import math
distancia= math.sqrt((x2-x1)**2+(y2-y1)**2)

print("Distancia: %.4f" % distancia)