#encoding: UTF-8

# Autor: Mirna Fernanda Zertuche Calvillo, A01373852
# Descripcion: Calcular el total de alumnos más porcentaje de hombres y de mujeres inscritos.

Mujeres= int(input("Mujeres inscritas:" ))
Hombres= int(input("Hombres inscritos:" ))
Total= Mujeres+Hombres
Pmujeres= float((Mujeres*100)/Total)
Phombres= float((Hombres*100)/Total)

print("Total de inscritos:", Total)
print("Porcentaje de mujeres:%.1f"% Pmujeres,"%")
print("Porcentaje de hombres:%.1f"% Phombres,"%")




