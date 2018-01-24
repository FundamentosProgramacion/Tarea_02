#encoding: UTF-8

# Autor: Andrés Reyes Rangel, A01746592
# Descripcion: Porcentaje de hombres y mujeres.

# A partir de aquí escribe tu programa

mujeres=int(input("Cuantos mujeres hay en la clase: "))
hombres=int(input("Cuantos hombres hay en la clase: "))

total= mujeres+hombres
porcentajeM= (mujeres*100)/total
porcentajeH=(hombres*100)/total

print("Total de inscritos: ", total)
print("Porcentaje de mujeres: %.1f" % porcentajeM)
print("Porcentaje de hombres: %.1f" % porcentajeH)
