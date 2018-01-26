#encoding: UTF-8

# Autor: Carlos Martínez Rodríguez
# Descripcion: Calcular el porcentaje de mujeres y hombres de inscritos en una clase

# A partir de aquí escribe tu programa
numeroMujeres = int(input("Número de mujeres inscritas: "))
numeroHombres = int(input("Número de hombres inscritos: "))

#Total de alumnos inscritos en la clase
totalAlumnos = numeroMujeres + numeroHombres

#Porcentaje de mujeres utilizando regla de tres
porcentajeMujeres = (numeroMujeres * 100) / totalAlumnos

#Porcentaje de hobres utilizando regla de tres
porcentajeHombres = (numeroHombres * 100) / totalAlumnos

#Salidas
print("Total de inscritos: ", totalAlumnos)
print("Porcentaje de mujeres: %0.1f" % porcentajeMujeres)
print("Porcentaje de hombres: %0.1f" % porcentajeHombres)