#----------------------------------------------------------------------------------------------------------------------

#encoding: UTF-8

# Autor: Sebastian Morales Martin, A01376228
# Descripcion: Calculo de total de una cuenta de restaurante considerando IVA y Propina

# Análisis
# Entrada: Subtotal de la cuenta
# Salida: Total de la cuenta con el IVA y la propina
# Relación E/S: el calculo del cubtotal para obtener el IVA y la propina


#----------------------------------------------------------------------------------------------------------------------

subT = float(input("Subtotal de la cuenta: "))

propela = subT * 0.12
iva = subT * 0.16

total = subT + propela + iva

print("Subtotal: %10.2f \nIVA: %10.2f \nPropina: %10.2f \nTOTAL: %10.2f" % (subT, iva, propela, total))
