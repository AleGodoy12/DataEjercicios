#1.- Crea un bucle while que se ejecute hasta que x valga 15 con incrementos de 5 

# num=0
# numeros= 15
# while num <= numeros:
#     print(num)
#     num+=5

#2.- Crea un bucle while que se ejecute hasta que x valga -100 con decrementos de 20.

# num=0
# numeros= -100
# while num >= numeros:
#     print(num)
#     num+= -20

  
#3.- Crea un bucle while que se ejecute hasta que x valga 0 con decrementos de 1 y que muestre en cada ejecución esta frase con el valor de ejecución correspondiente: 'El valor del bucle es 10'...
# x = int(input("numero: "))
# num=0

# while x >= num:
#      print("el valor del bucle es ", x) 
#      x-= 1



#4.- Crea un bucle for que itere la siguiente tupla y muestre una frase como esta en cada iteración: 'El color es: ' + color + '.'

# lista = ["verde", "amarillo", "rojo", "azul"]

# for color in lista:
#     print ("El color es " + color + ".")

#5.- Crea un bucle for con un range() que vaya desde el valor 7 hasta el valor 700 en saltos de 100. Basta con que imprimas el valor de cada iteración.
# inicio = 7
# limite = 708

# def iteracion (numero):
 

#     for iterar in range (numero, limite, 100):
#             print (iterar)

# iteracion(inicio)

#Opcional-

#**Crea un bucle while con las siguientes características:
# El valor inicial de la variable x será de 0.                
# El valor de incremento será 1.                               
# La condición de salida del bucle será mayor o igual a 30.    
# La ejecución se deberá romper cuando x valga 15.   break x = 15 
# Debes imprimir la siguiente frase cada vez que se ejecute el bucle: 'El valor del bucle es: ' + x.
# Debes saltarte las ejecuciones con valor de x en 4, 6 y 10.
# En cada salto de ejecución, deberás mostrar los valores saltado con este mensaje: 'Se saltó el valor ' + x ' de x'.
# Cuando se rompa la ejecución del bucle deberás mostrar un mensaje indicándolo: 'Se rompió la ejecución del bucle cuando x valía ' + x **

x = 0
incremento = 1

while x <= 30:
    print("el valor del bucle es: " + x)
    


    