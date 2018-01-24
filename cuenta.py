#encoding: Phyton

# Autor: Guillermo Adrian Urbina Aguiñiga, A01746645
# Descripcion: Este programa te dice el IVA, Propina y cuenta a pagar 

Cuenta = int(input("Teclea tu cuenta: "))
 
Propina = Cuenta * .13
IVA = Cuenta * .15
Total = Propina + IVA + Cuenta

print("Propina= "format(Propina,".2"))
print("IVA= "format(IVA,".2"))
print("Total= "format(Total,".2"))
             

