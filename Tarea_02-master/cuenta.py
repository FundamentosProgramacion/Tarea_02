#encoding: UTF-8

# Autor: Carlos Ochoa, A01746583
# Descripcion: Determina el costo total de la comida dado su valor inicial

# A partir de aquí escribe tu programa

cuenta_comida=int(input("Cuanto fue la cuenta de la comida: "))
print cuenta_comida
print "Propina: ", cuenta_comida*.13
print "IVA: ", cuenta_comida*.15
print "Total a pagar: ", cuenta_comida+cuenta_comida*.13+cuenta_comida*.15
