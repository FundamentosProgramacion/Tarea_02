#encoding: UTF-8

# Autor: Jorge Mora Cárdenas A01746123
# Descripcion: distancia que recorre un auto dada la velocidad que lleva.

# A partir de aquí escribe tu programa

velocidad = int(input("Dame la velocidad del vehículo(Km/h): "))

distancia = 7 * velocidad
distancia2 = 4.5 * velocidad
tiempo = 500 / velocidad

print("La distancia recorrida en 7 horas es de: %.1f" % distancia, "km")
print("La distancia recorrida en 4.5 horas es de: %.1f"% distancia2, "km")
print("El tiempo que se emplea para recorrer 500 km es de: %.1f"% tiempo, "h")

