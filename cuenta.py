#Autor: Nataly Paulina Lopez Salazar
#Se va calcular la cueta de una comida con popina e iva.

st=int(input("Costo de la comida: "))

p = st* .13
iva = st * .15
t = st+p+iva

print("Propina: ",p)
print("IVA: ",iva)
print("El total de su consumo es: ",t)
