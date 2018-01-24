##Autor: David Medina Medina  A01653311
##Porcentaje de hombres y mujeres
mujeres = int(input("Ingrese numero de mujeres inscritas:"))
hombres = int(input("Ingrese numero de hombres inscritos:"))
nTotal = hombres+mujeres
porcentajeM = mujeres/nTotal*100
porcentajeH = hombres/nTotal*100
print("El numero total de alumnos es:",nTotal)
print("El porcentaje de mujeres es: %.1f" % porcentajeM)
print("El porcentaje de hombres es: %.1f" % porcentajeH)
