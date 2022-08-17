# Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para 
# decidirlo. Una dirección se considerará válida si contiene el símbolo "@"

# pregunta = input("Ingrese su direccion de gmail: ")
# arr = "@"
# def num(pregunta):                          
#     for i in pregunta:
#         if i == arr:
#             return "El mail es valido"
#     return "La direccion no es valida"
# mail = num(pregunta)
# print(mail)



# 2. Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice dicha suma)

# def suma(n):
#     sum = [int(x) for x in str(n)]
#     b = 0
#     for i in sum:
#         b += i 
#     return b 
# numero = int(input("Ingrese un numero: "))
# while numero != 0:
#     print(suma(numero))
#     numero = int(input("Ingrese un numero: "))
# print("Finaliza")


# def  sumadigitos (a) : # defino funcion (a) puede val
#     digitos =[int (x) for x in str(a)]   #va a leer el elemento
#     acumulador = 0   #declaro el acumulador ene su posicion 

#     for i in digitos:  
  

#         acumulador+=i 
#     return acumulador
# numero = input("ingrese un numero")
# while numero !="0": # cero como string 
#     print (sumadigitos(numero))
#     numero = input("ingrese un numero")

# print ("bucle finalizado")

# while numero != x:
#     if numero > x:
#         numero = int(input("Ingrese un numero: "))                       # Sobrescribe la variable
#     if numero == x:
#         break
# print("Bucle finalizado")



# 3. Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos. Al finalizar, mostrar la sumatoria 
# de todos los números ingresados y la suma de sus dígitos. Reutilizar la misma función realizada en el ejercicio 2,

def suma(n):
    sum = [int(x) for x in str(n)]
    b = 0
    for i in sum:
        b += i 
    return b 
numero = int(input("Ingrese un numero: "))
while numero != 0:
    print(suma(numero))
    numero = int(input("Ingrese un numero: "))
print("Finaliza")


