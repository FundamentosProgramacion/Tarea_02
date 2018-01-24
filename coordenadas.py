##Autor: David Medina Medina
##Coordenadas
import math
x1 = int(input("Ingresar coordenadas de x1:"))
y1 = int(input("Ingresar coordenadas de y1:"))
x2 = int(input("Ingresar coordenadas de x2:"))
y2 = int(input("Ingresar coordenadas de y2:"))
distancia = math.sqrt((x2-x1)**2+(y2-y1)**2)
print ("distancia %.4f" % distancia)
