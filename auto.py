#encoding: UTF-8
# Autor: Genaro Ortiz Durán, A01375315
# Descripcion: Calcular las distancias que recorre un auto en distintas horas y el tiempo que tarda en recorrer una distancia.

velocidad=float(input("Introduce la velocidad del auto:"))
distancia=velocidad*7
distancia1=velocidad*4.5
tiempo=437/velocidad

print("La distancia recorrida en 7 horas es de:",format(distancia,".1f"), "km")
print("La distancia recorrida en 4.5 horas es de:",format(distancia1,".1f"),"km",)
print("El tiempo que toma recorrer 437 km es de:",format (tiempo, ".1f"))

pri