##Autor: David Medina A01653311
##Realizar cuenta con iva y propina
cuenta = float(input("Ingrese subtotal de su cuenta en pesos:"))
iva = cuenta*0.15
propina = cuenta*0.13
cuentaTotal = cuenta+propina+iva
print("Costo de su comida: %.1i" % cuenta)
print("Propina: %.2f" % propina,"pesos")
print("IVA: %.2f" % iva,"pesos")
print("Su total a pagar es: %.2f" % cuentaTotal,"pesos")
