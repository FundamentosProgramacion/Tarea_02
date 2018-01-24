#encoding: UTF-8
# Autor: Genaro Ortiz Durán, A01375315
# Descripcion: Calcular el costo total de una comida.

totalComida=int(input("¿Cuál fue el total de la comida?:"))
propina= totalComida*0.13
IVA=totalComida*0.15
total=totalComida+propina+IVA

print("Costo por la comida:",totalComida,"$")
print("Propina:","$",format(propina,".2f"))
print("IVA:","$",format(IVA,".2f"))
print("Costo total de la comida:","$",format(total,".2f"))

