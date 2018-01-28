# Autor: Jean Paul Esquivel Lobato, A01376152
# Descripcion: Encontrar distancia recorrida.

velocidad = float(input("¿A qué velocidad viaja el auto que ves? (km/h):"))
distancia7 = velocidad * 7
distancia4 = velocidad * 4.5
tiempo437 = 437 / velocidad

print("En 7hrs, se recorre", distancia7, "km")

print("En 10hrs, se recorre", distancia4, "km")

print("Para recorrer 437 km, se necesita ", round(tiempo437, 2), "hrs")
