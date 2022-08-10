# Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para 
# decidirlo. Una dirección se considerará válida si contiene el símbolo "@"

pregunta = input("Ingrese su direccion de gmail: ")
arr = "@"

def num(arr):
    for i in pregunta:
        if i == arr:
            return "El mail es valido"
        else:
            print(arr in pregunta, "La direccion no es valida")
mail = num(arr)
print(mail)



# 2. Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice dicha suma)

# numero = int(input("Ingrese un numero: "))
# numero2 = int(input("Ingrese un numero: "))
# # def sum(numero, numero2):
# while numero + numero2:
#     numero + numero2
#     numero == 0
#     break




    
#     suma2 = numero + numero2
#     return suma2
# suma = numero + numero2
#print(suma)





# 3. Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos. Al finalizar, mostrar la sumatoria 
# de todos los números ingresados y la suma de sus dígitos. Reutilizar la misma función realizada en el ejercicio 2,
