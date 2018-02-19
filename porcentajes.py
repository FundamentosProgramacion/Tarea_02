#encoding: UTF-8

# Autor: Jorge Mora Cárdenas  A01746123
# Descripcion: porcentaje de hombres y mujeres en un salon de clases.

# A partir de aquí escribe tu programa
mujeres = int(input("Mujeres inscritas: "))
hombres = int(input("Hombres inscritos: "))

total = mujeres + hombres
porcentajeMujeres = mujeres * 100 / total
porcentajeHombres = hombres * 100 / total

print("Total de inscritos: ",total)
print("Porcentaje de mujeres: %.1f"% porcentajeMujeres)
print("Porcentaje de hombres: %.1f"% porcentajeHombres)
