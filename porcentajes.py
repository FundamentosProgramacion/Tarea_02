#encoding: UTF-8
# Autor: Genaro Ortiz Durán, A0137515
# Descripcion: Escribir un programa que calcule el porcentaje de hombres y mujeres que hay en una clase.

hombres=int(input("¿Cuántos hombres hay en la clase?:"))
mujeres=int(input("¿Cuántas mujeres hay en la clase?:"))
total=hombres+mujeres
porcentajeHombres=hombres*100/total
porcentajeMujeres=mujeres*100/total

print("Total de alumnos:",total)
print("Porcentaje de hombres",format(porcentajeHombres,".2f"),"%")
print("Porcentaje de mujeres",format(porcentajeMujeres,".2f"),"%")




