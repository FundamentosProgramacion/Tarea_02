#encoding: UTF-8

# Autor: Sebastian Morales Martin
# Descripcion: Ejercicio de Coordenadas

# A partir de aquí escribe tu programa

import math as mat

x1 = float(input("X1: "))
y1 = float(input("Y1: "))
x2 = float(input("X2: "))
y2 = float(input("Y2: "))

d = mat.sqrt(((x2-x1)**2)+((y2-y1)**2))

print("La distancia entre el punto (%i, %i) y (%i, %i) es de: %.2f" % (x1, y1, x2, y2, d))