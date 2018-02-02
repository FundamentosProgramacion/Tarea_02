#encoding: UTF-8

# Autor: Karla Fabiola Ramirez Martinez
# Descripcion: Un programa que pueda calcular el IVA y la propina para de esta manera imprimir el total a pagar

comida= int(input("Dime el total de la comida: "))
iva=comida*0.15
propina=comida*0.13
total=propina+iva+comida
print ("Propina: ",propina)
print("IVA: ",iva )
print ("Total a pagar: ",total)


