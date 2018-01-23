#encoding: UTF-8

# Autor: Mirna Fernanda Zertuche Calvillo, A01373852
# Descripcion: Dar el IVA, la propina y el costo total de una comida deacuerdo al costo dado.

Comida= float(input("Costo de la comida: "))
IVA= Comida*0.15
Propina= Comida*0.13
CostoTotal= Comida+IVA+Propina

print("Costo de su comida:$%.2f"% Comida)
print("Propina:$%.2f"% Propina)
print("IVA:$%.2f"% IVA)
print("Total a pagar:$%.2f"% CostoTotal)
