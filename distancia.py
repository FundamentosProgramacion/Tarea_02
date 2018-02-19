#Autor: Nataly Paulina Lopez Salazar
#SE va calcular la disyancia de 2 puntos
import math
print("Distancia entre dos puntos")
x1= int(input("Dame el valor de x1: "))
x2= int(input("Dame el valor de x2: "))
y1= int(input("Dame el valor de y1: "))
y2= int(input("Dame el valor de y2: "))

d = math.sqrt(((x2-x1)**2)+((y2-y1)**2) )

print("El valor de la distancia es: %.2f"%d)
