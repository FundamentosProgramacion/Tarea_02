#Fernando Sebastian Silva Miramontes, A01746925
#Se Calcula la distancia entre dos puntos de una recta.
x1 = int(input("Dame el valor de X del primer punto.\n"))
y1 = int(input("Dame el valor de X del primer punto.\n"))
x2 = int(input("Dame el valor de X del primer punto.\n"))
y2 = int(input("Dame el valor de X del primer punto.\n"))
raizC = (x2-x1)**2+(y2-y1)**2
distancia = raizC**.5
print("La distancia entre las coordenadas otorgada es: "+str(distancia))