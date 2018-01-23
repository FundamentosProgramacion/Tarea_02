#encoding: UTF-8

# Autor: Fernando Sebastian Silva Miramontes, A01746925
# Descripcion: Calcular porcentaje de hombres y mujeres de una poblacion estudiantil

numDeM = float(input("Cuantas mujeres hay?\n"))
numDeH = float(input("Cuantos hombres hay?\n"))
total = numDeH+numDeM
porcDeM = numDeM/total *100
porcDeH = numDeH/total *100
print("Hay "+str(total)+" estudiantes inscritos")
print("El "+str(porcDeM)+"% son mujeres")
print("El "+str(porcDeH)+"% son hombres")
