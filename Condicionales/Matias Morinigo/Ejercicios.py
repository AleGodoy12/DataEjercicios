# 1- Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

pregunta = int(input("Ingrese su edad: "))
edadMayor = 18
if pregunta >= edadMayor:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")


# 2.- Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
# Si el divisor es cero el programa debe mostrar un error.

numero = int(input("Ingrese un numero: "))
num = int(input("Ingrese un numero: "))

if numero / num:
    numero /= num
    print(numero)
else:
    ("Error")

# 3.- Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar

numeroPedi = int(input("Ingrese un numero entero: "))

if numeroPedi % 2 == 0:    #%2 Sirve para comparar si es divisible por 0
    print("Es par")
else:
    print("Es impar")


#  La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
#  Los ingredientes para cada tipo de pizza aparecen a continuación.

# pregunta = input("Que tipo de pizza quiere ?: ")
# respuesta = "vegetariana"
# pizzaVege = ["Pimiento y tofu"]
# pizzaNoVege = ["Peperoni, Jamón y Salmón"]

if pregunta == respuesta :
    print("Estos son sus ingredientes: ", pizzaVege)
else: 
    print("Estos son sus ingredientes: ", pizzaNoVege)


pregunta = input("Quiere una pizza vegetariana o normal ? ")   
respue1 = "vegetariana"
pizzaVege = ["pimiento o tofu"]
pizzaNoVege = ["Peperoni, Jamón o Salmón"]
if pregunta == respue1:
    print("Elija un ingrediente: ", pizzaVege)
else:
    print("Elija un ingrediente: ", pizzaNoVege)
pregunta2 = input("Cual elijira: ")
vege = [pizzaVege]
noVege = [pizzaNoVege]
if pregunta2 == vege:
    print("Su pizza es vegetariana y su ingredinete es: ", pregunta2)
else:
    print("Su pizza no es vegetariana y su ingredinte es: ", pregunta2)