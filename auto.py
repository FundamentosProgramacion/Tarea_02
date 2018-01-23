#encoding: UTF-8

# Autor: Mirna Fernanda Zertuche Calvillo, A01373852
# Descripcion: Un programa que a partir de la velocidad dada calcula: distancia recorrida en 7 y 4.5 hrs y tiempo en que recorre 437km.

Velocidad= float( input("Velocidad: "))
Distancia7= Velocidad*7
Distancia4= Velocidad*4.5
Tiempo= 437/ Velocidad

print("Distancia recorrida 7 horas: %.1f" % Distancia7,"km")
print("Distancia recorrida 4.5 horas: %.1f" % Distancia4,"km")
print("Tiempo para reocrrer 437km : %.1f" % Tiempo,"hrs")
