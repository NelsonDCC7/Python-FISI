lista_numeros=[]

for a in range(10):
      numero=float(input("Ingrese el valor  "+str(a+1) +" :" ))

      lista_numeros.append(numero)

print("\n\nLIsta de 10 numeros aleatorios")
print(lista_numeros)

lista_numeros1=[]

for b in lista_numeros:
      numero1=pow(b,3)

      lista_numeros1.append(numero1)

print("\n\nLIsta de 10 numeros aleatorios al cubo")

print(lista_numeros1)

lista_numeros2=[]

for c in lista_numeros:
      numero2=pow(c,2)

      lista_numeros2.append(numero2)

print("\n\nLIsta de 10 numeros aleatorios al cuadrado ")
print(lista_numeros2)

suma_de_listas=lista_numeros1+lista_numeros2

print("\n\nSuma de las dos listas anteriores")
print(suma_de_listas)

suma_de_listas.reverse()
print("\n\nLa  nueva lista inversa ")
print(suma_de_listas)
