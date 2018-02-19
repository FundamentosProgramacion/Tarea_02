#encoding: UTF-8

# Autor: Jorge Mora Cárdenas  A01746123
# Descripcion: da el total y el desgloce al pagar en la cuenta de un restaurante.

# A partir de aquí escribe tu programa

costo = int(input("¿Cuál es el costo de tu comida? "))

propina = .13 * costo
iva = .15 * costo
total = costo + propina + iva

print("propina: $%.2f" % propina)
print("IVA: $%.2f"% iva)
print("Total a pagar: $%.2f"% total)

