# Autor: Diana Patricia Aguilar Martínez, A01745778
# Descripcion:  Este programa calcula la distancia entre un punto y otro
# A partir de aquí escribe tu programa

x1=int(input("x1: "))
y1=int(input("y1: "))

x2=int(input("x2: "))
y2=int(input("y2: "))

distancia = (((x2 - x1)**2 + (y2 - y1)**2 ) **0.5)

print("la distancia entre los dos puntos es: %.4f"%distancia)

