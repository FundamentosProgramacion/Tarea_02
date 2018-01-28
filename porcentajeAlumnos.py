#Jean Paul Esquivel Lobato
#A01376152
#Calcula el porcentaje de hombres y mujeres inscritos en una clase.

mujeres = int(input("Teclea las mujeres inscritas:"))
hombres = int(input("Teclea los hombres inscritos:"))

totalAlumnos = mujeres + hombres
porcentajehombres = (hombres*100)/totalAlumnos
porcentajemujeres=  (mujeres*100)/totalAlumnos

print("El total de alumnos inscritos son:", totalAlumnos)
print("El porcentaje de mujeres son %.1f" % porcentajemujeres,"%")
print("El porcentaje de hombres son %.1f" % porcentajehombres,"%")