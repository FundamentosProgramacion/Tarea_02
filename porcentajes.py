#----------------------------------------------------------------------------------------------------------------------

#encoding: UTF-8

# Autor: Sebastian Morales Martin, A01376228
# Descripcion: Calcula el porcentaje de hombres y mujeres en un salon

# Análisis
# Entrada: número de hombres y mujeres en el salón
# Salida: Número total de alumnos, porcentaje de hombres y mujeres
# Relación E/S: Fórmula para el porcentaje de niño/as en el salón, suma de ambos sexos para dar el total de alumnos

#----------------------------------------------------------------------------------------------------------------------

hom = int(input("Hombres en el salón: "))

print("\n")
print("------------------------------------------------------------")
print("\n")

muj = int(input("Mujeres en el salón: "))

print("\n")
print("------------------------------------------------------------")
print("\n")

totalAlum = hom + muj

porHom = (hom*100)/totalAlum
porMuj = (muj*100)/totalAlum

print("1. Total de Alumnos: %10.2f \nPorcentaje de Hombres: %10.2f % \nPorcentaje de Mujeres: %10.2f % \n")
print("------------------------------------------------------------")
