dic={}

nombre=input("Ingrese el nombre : ")
apellido=input("Ingrese su apellido :")
edad=int(input("Ingrese su edad :"))
dni=int(input("Ingrese su DNI :"))

dic["Nombre"] =nombre
dic["Apellido"] =apellido
dic["Edad"] =edad
dic["DNI"] =dni

print(dic)

print(dic.values())

profesion=input("Ingrese su profesion:")
dic["profesion"]=profesion

print(dic)

