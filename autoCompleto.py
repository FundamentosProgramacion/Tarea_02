# Autor: Diana Patricia Aguilar Martínez, A01745778
# Descripcion:  Este programa calcula la distancia que un auto a cierta velocidad y la velocidad que necesita para recorrer ciertos kilometros
# A partir de aquí escribe tu programa

v= int(input("inserte la velocidad de su auto (km/h): "))
d1= v*7
d2 = v*4.5
t1= 437/v

print ("la distancia que recorre en 7 horas es de:%.1f"% d1,"km")
print ("la distancia que recorre en 4.5 horas es de:%.1f"% d2,"km")
print ("el auto tarda %.1f"% t1,"horas en recorrer 437 kilometros ")