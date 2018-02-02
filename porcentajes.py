#encoding: UTF-8

# Autor: Karla Fabiola Ramirez Martinez
# Descripcion: Porcentaje hombres y mujeres

mujeres=int(input("Dime el numero de mujeres que hay: "))
hombres=int(input("Dime el numero de hombres que hay: "))
total=mujeres+hombres
porcentaje=100/total
pmujeres=porcentaje*mujeres
phombres=porcentaje*hombres

print("Porcentaje de hombres: %5.2f "%phombres)
print("Porcentaje de mujeres: %5.2f "%pmujeres)
print("Total de alumnos: ",total)

