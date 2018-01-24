#encoding: UTF-8

# Autor: Alejandro Valenzuela Guerrero, A01339478
# Descripcion: Calcular distancia entre dos puntos
# A partir de aquí escribe tu programa

x1 = input("Coordenada x1:")
y1 = input("Coordenada y1:")
x2 = input("Coordenada x2:")
y2 = input("Coordenada y2:")
distancia = (((float(x2) - float(x1))**2)+((float(y2) - float(y1))**2))**.5
print("La distancia es de:", distancia)
