#encoding: UTF-8

# Autor: Ricardo Cornejo Lozano, A01746439
# Descripcion: Calcula distancia en 7,4.5 horas y calcula tiempo para recorrer 500km ingresando la velocidad 

# A partir de aquí escribe tu programa

velocidad = int(input("ingresa la velocidad"))
t1 = int(7)
t2 = float(4.5)
tiempoPara = 500/velocidad
dis1 = float(velocidad*t1)
dis2 = velocidad*t2
print ("Distacia en 7hrs:%.1f" % int(dis1), "km")
print ("Distacia en 4hrs:", float(dis2),"km")
print ("Tiempo para recorrer 500km: %.1f" % tiempoPara,"hrs")


