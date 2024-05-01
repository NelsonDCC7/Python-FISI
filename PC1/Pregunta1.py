
lista=[]
nombre=input("Ingrese su nombre:")
apellido=input("Ingrese su apellido:")
edad=int(input("Ingrese la edad:"))

completo="El nombre completo es : "+nombre +" " +apellido +" "

print(completo)

print("Los tipos de datos ingresados son {} {} {}".format(type(nombre),type(apellido),type(edad)))

for a in range(2):
     nombre1=input("Ingrese el nombre del trabajador  "+str(a+1) +" :" )
     edad1=int(input("Ingrese la edad del trabajador  "+str(a+1) +" :"))
     lista.append([nombre1,edad1])

print(lista)











