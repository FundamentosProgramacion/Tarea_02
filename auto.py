#encoding: UTF-8

# Autor: Andrés Reyes Rangel, A01746592
# Descripcion: Calcular distancia y tiempo.

# A partir de aquí escribe tu programa

v=float(input("Velocidad del auto en km/hr: "))

d1=v*7
d2=v*4.5
t=437/v

print("Distancia recorrida en 7 hrs: %.1f" % d1)
print("Distancia recorrida en 4.5 hrs: %.1f" % d2)
print("Tiempo para recorrer 500 km: %.1f" % t)
