#Autor:Karla Fabiola Ramirez Martinez
#Descripcion: Distancia entre dos puntos

x1=int(input("Dame la x del primer punto: "))
y1=int(input("Dame la y del primer punto: "))
x2=int(input("Dame la x del segundo punto: "))
y2=int(input("Dame la y del segundo puntp: "))

x=(x2-x1)**2
y=(y2-y1)**2
distancia=(x+y)**0.5

print("Distancia: ",distancia)