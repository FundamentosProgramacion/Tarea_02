costo = float(input("�Cu�nto cost� la comida que compraste?"))

IVA = costo * 0.13
propina = costo * 0.15
costoTotal = costo + IVA + propina


print("Tu subtotal fue de: $", costo)

print("El IVA fue: $", round(IVA, 2))

print("La propina es: $", round(propina, 2))

print("El total es: $", round(costoTotal, 2))
