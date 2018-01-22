#----------------------------------------------------------------------------------------------------------------------

#encoding: UTF-8

# Autor: Sebastian Morales Martin, A01376228
# Descripcion: Distancias de un auto con respecto a su velocidad

# Análisis
# Entrada: Constantes de distancia y tiempo
# Salida: Aprximado de la velocidad en cada uno de los casos y el tiempo en el tercer caso
# relación E/S: Cálculo de la velocidad, tiempo, y distancia

#----------------------------------------------------------------------------------------------------------------------


vel = float(input("Velocidad: "))

distancia6Horas = vel*6
distancia10Horas = vel*10
tiempo500Kilometros = 500/vel

print("-----------------------------------------------------------")
print("\n")

print("1. Distancia en 6 Horas:")
print("-", distancia6Horas)

print("\n")

print("2. Distancia 10 Horas")
print("-", distancia10Horas)

print("\n")

print("3. Tiempo para alcanzar los 500 km:")
print("-", tiempo500Kilometros, "hora/s aprox.")

print("\n")

print("-----------------------------------------------------------")
