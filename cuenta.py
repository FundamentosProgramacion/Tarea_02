#encoding: UTF-8

# Autor: Andrés Reyes Rangel, A01746592
# Descripcion: Calcular el total de una comida.

# A partir de aquí escribe tu programa

subtotal=float(input("Ingresa el costo de tu comida: "))

propina=subtotal*0.13
IVA=subtotal*0.15
total=propina+subtotal+IVA

print("Subtotal: $%.2f" % subtotal)
print("Propina: $%.2f" % propina)
print("IVA: $%.2F" % IVA)
print("Total a pagar: $%.2f" % total)
