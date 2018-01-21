mujeres=int(input("Cuál es el número de mujeres inscritas?"))
hombres=int(input("Cuál es el número de hombres inscritos?"))
TotalAlumnos=mujeres+hombres
PorcentajeMujeres=(mujeres*100)/TotalAlumnos
PorcentajeHombres=(hombres*100)/TotalAlumnos
print("Total inscritos: %.02f"%TotalAlumnos,"\nPorcentaje mujeres:  %.02f%%"%PorcentajeMujeres,"\nPorcentaje hombres:  %.02f%%"%PorcentajeHombres)