#encoding: UTF-8

# Autor: Mirna Fernanda Zertuche Calvillo, A01373852
# Descripcion: A partir de las coordenadas de dos puntos dados se determina la distancia que existe entre estos.

x1= float(input("X1: "))
y1= float(input("Y1: "))
x2= float(input("X2: "))
y2= float(input("Y2: "))

distanciaFinal= ((x2-x1)**2+(y2-y1)**2)**0.5

print("Distancia: %.4f" % distanciaFinal)