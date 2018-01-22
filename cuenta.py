#encoding: UTF-8

# Autor:Fernando Sebastian Silva Miramontes, A01746925
# Descripcion: Caclular el costo total de una comida que incluya la propina y el IVA

subtotal = float(input("Cuanto le costo la comida?\n"))
iva = subtotal*0.15
propina = subtotal*0.13
costoTotal = subtotal+iva+propina
print("Costo de su comida: ",subtotal)
print("IVA: ",iva)
print("Propina: ",propina)
print("Costo Total: ",costoTotal)
