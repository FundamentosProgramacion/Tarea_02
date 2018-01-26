#encoding: UTF-8

# Autor: Carlos Martínez Rodríguez
# Descripcion: Calcula la distancia recorrido de un auto en horas

# A partir de aquí escribe tu programa

#Leer Velocidad
velocidad = int(input("Velocidad del auto en km/h: "))
#Distnacia que recorre en 7 horas
distancia1 = velocidad * 7
#Distnacia que recorre en 4.5 horas
distancia2 = velocidad * 4.5
#Tiempo que tarda en recorer 473km
distancia3 = 473 / velocidad

print("Distancia recorrida en 7 hrs: ", distancia1)
print("Distancia recorrida en 4.5 hrs: ", distancia2)
print("Tiempo para recorrer 473 km: ", distancia3)

