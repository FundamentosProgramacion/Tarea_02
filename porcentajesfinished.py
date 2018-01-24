#encoding: UTF-8

# Autor: Ricardo Cornejo Lozano, A01746439
# Descripcion: Calcula porcentaje de hombres y mujeres.

# A partir de aquí escribe tu programa

mujeres = int(input("Teclea el numero de mujeres inscritas: "))
hombres = int(input("Teclea el numero de hombres inscritos: "))
porcentajeMujeres = float((mujeres*100)/(mujeres+hombres))
porcentajeHombres = float(hombres*100)/(mujeres+hombres)
print ("Total de inscritos: " +str(mujeres+hombres), "\nPorcetaje de mujeres:%.1f%%" % +float(porcentajeMujeres), "\nPorcentaje de hombres: %.1f%%" % +float(porcentajeHombres))
