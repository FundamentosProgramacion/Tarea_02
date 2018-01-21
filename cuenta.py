Total=int(input("Cuál es el costo total de la comida"))
Propina=Total*0.13
IVA=Total*0.15
TotalPagar=Propina+IVA+Total
print("Propina: $%.02f"%Propina,"\nIVA: $%.02f"%IVA,"\nTotal a pagar: $%.02f"%TotalPagar)