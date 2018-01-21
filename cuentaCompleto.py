# Autor: Diana Patricia Aguilar Martínez, A01745778
# Descripcion:  Este programa calcula la propina, el IVA y el costo total de una comida
# A partir de aquí escribe tu programa

subtotal=float(input("¿cual es le costo de su comida? "))

propina= subtotal*0.13
iva= subtotal*0.15
total= subtotal + propina + iva

print ("propina:$%.2f"% propina )
print ("iva: $%.2f"% iva)
print ("total: $%.2f " % total)
