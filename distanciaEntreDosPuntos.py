#Jean Paul Esquivel Lobato
#A01376152
#Calcula la distancia entre dos puntos.

print ("Teclea las coordenadas X1 y Y1 para el primer punto")
x1 = int(input("x1:"))
y1 = int(input("y1:"))
print ("Teclea las coordenadas X2 y Y2 para el segundo punto")
x2 = int(input("x2:"))
y2 = int(input("y2:"))

distancia = (((x2 - x1)**2) + ((y2 - y1)**2))**0.5

print("La distancia entre tus dos puntos es: %.4f"% distancia)
