#Autor: Nataly Paulina Lopez Salazar
#Se va calcular el porcentaje de hombres y mujeres

m=int(input("Numero de mujeres: "))
h=int(input("Numero de hombres: "))

t=m+h
pm= (m*100)/t
ph= (h*100)/t

print("Total de inscritos: ",t)
print("Porcentaje de mujeres: %.2f%%"%pm)
print("Porcentaje de hombres: %.2f%%"%ph)
