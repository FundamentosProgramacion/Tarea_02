# Autor: Diana Patricia Aguilar Martínez, A01745778
# Descripcion:  Este programa calcula el procentaje de hombres y de mujeres.
# A partir de aquí escribe tu programa

mujeres=int(input("¿cuantas mujeres hay inscritas? "))
hombres= int(input("¿cuantos hombres hya inscritos? "))

total= mujeres + hombres
porcentajeMujeres= (mujeres/total)*100
porcentajeHombres= (hombres/total)*100

print("Total de alumnos: %.1f"%total)
print("Porcentaje de mujeres inscritas: %.1f"%porcentajeMujeres,"%")
print("Porcentaje de hombres inscritos: %.1f"%porcentajeHombres,"%")
