#encoding: UTF-8

# Autor: Jorge Mora Cárdenas  A01746123
# Descripcion: Encontrar la distancia entre dos coordenadas.

# A partir de aquí escribe tu programa

x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

distancia =( (x2 - x1)**2 + (y2 - y1)**2) * 0.5

print("Distancia: %.4f"% distancia)
