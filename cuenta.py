#encoding: UTF-8

# Autor: Carlos Martínez Rodríguez
# Descripcion: Calcula la cuenta total de un restaurante sumando el iva y la propina

# A partir de aquí escribe tu programa

costoCuenta = int(input("Costo de su comida: "))
#Calcular el iva de la cuenta IVA = 16%
iva = costoCuenta * 0.16
#Calcular la propina de la cuenta propina = 13%
propina = costoCuenta * 0.13

costoTotal = costoCuenta + propina + iva

#Salidas
print("Propina: $%.2f" % propina)
print("IVA: $%.2f" % iva)
print("Total a pagar: $%.2f" % costoTotal)
