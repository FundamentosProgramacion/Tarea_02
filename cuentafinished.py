#encoding: UTF-8

# Autor: Ricardo Cornejo Lozano, A01746439
# Descripcion: Calcula el total incluyendo IVA y propina.

# A partir de aquí escribe tu programa

totalNeto = int(input("Teclea el costo de su comida:"))
propina = totalNeto * .13
iva = totalNeto * .15
totalFinal = totalNeto + propina + iva
print("Costo de su comida: " + str(totalNeto), "\nPropina: " +str(propina), "\nIVA: " +str(iva), "\nTotal a Pagar: " +str(totalFinal))




