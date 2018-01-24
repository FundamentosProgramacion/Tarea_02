#encoding: UTF-8
# Autor: Genaro Ortiz Durán, A01375315
# Descripcion: Escribir un programa que calcule la distancia entre dos puntos.

x1=float(input("Escribe la coordenada x:"))
y1=float(input("Escribe la coordena y:"))
x2=float(input("Escribe la coordenada x2:"))
y2=float(input("Escribe la coordenada y2:"))
distancia=((x2-x1)**2+(y2-y1)**2)**0.5

print("Distancia entre los puntos:",format(distancia,".4f"))