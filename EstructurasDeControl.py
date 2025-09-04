#Autor: Juan Camilo Páez Guaspud
#Ejercicios de Practica: 

#Ejercicio 1 (Imprime una frase)
print("Hola, ya sé imprimir frases en Python")

#Ejercicio 3 (Imprime un numero decimal)
float(print(3.14))

#Ejercicio 4 (Imprime la suma de dos numeros)
base=int(input("Ingresa un numero base:"))
suma=int(input("Ingresa un numero para sumar:"))

print("El resultado de la suma es:",base+suma)

#Ejercicio 8 (Imprime los numeros del 1 al 3)
for i in range(1,4):
    print(i)

#Ejercicio 10 (Imprime los numeros del 1 al 10000)
for e in range(1,10001):
   print(e)

#Ejercicio 14 (Imprime "Hola" 200 veces)
for i in range(200):
   print("Hola")

#Ejercicio 15 (Imprime los cuadrados de los numeros del 1 al 30)
for i in range(1,31):
    print(i**2)

#Ejercicio 16 (Imprime el factorial de 20)
resultado=1
for i in range(1,21):
    resultado *= i
print("El factorial de 20 es:",resultado)

#Ejercicio 17 (Imprime la suma de los cuadrados de los primeros 100 numeros)
resultado=1
for i in range(1,101):
    resultado += i**2
print("La suma de los cuadrados de los primeros 100 numeros es:",resultado)

#Ejercicio 18 ()
num=int(input("Escriba un numero entero"))
suma=0
for i in range(1,101):
    suma+=num+i
print("El resultado de la suma de tu numero a los 100 numeros siguientes es:",suma)

#Ejercicio 19 (Recibira un valor en euros y los convertira a dolares)
euros=float(input("Escriba la cantidad de euros que desea convertir a dolares:"))
dolares=euros*1.17
print(euros,"euros son",dolares,"dolares")

#Ejercicio 20 (Calcula el area de un triangulo)
alt=float(input("Escriba la altura del triangulo en decimales:"))
base=float(input("Escriba la base del triangulo en decimales:"))
area=(base*alt)/2
print("El area del triangulo es:",area)

#Ejercicio 21 (Imprime el numero mayor y menor entre dos numeros dados por el usuario)
num=int(input("Escriba un numero entero"))
num2=int(input("Escriba otro numero entero"))
if num>num2:
    print("El numero mayor es:",num)
    print("El numero menor es:",num2)
elif num2>num:
    print("El numero mayor es:",num2)
    print("El numero menor es:",num)
else:
     print("Los numeros son iguales")

#Ejercicio 22 (Imprime todos los numero impares menores que el numero recibido por consola)
num=int(input("Escriba un numero entero"))
for i in range(1,num+1,2):
    print(i)

#Ejercicio 26 (Imprime los tres numeros dados por el usuario ordenados de mayor a menor) 
num1=int(input("Escriba un numero entero"))
num2=int(input("Escriba otro numero entero"))
num3=int(input("Escriba un ultimo numero entero"))
if num1>num2 and num1>num3:
    if num2>num3:
        print("Ordenados de Mayor a menor:",num1,num2,num3)
    else:
        print("Ordenados de Mayor a menor:",num1,num3,num2)
elif num2>1 and num2>num3:
    if num1>num3:
        print("Ordenados de Mayor a menor:",num2,num1,num3)
    else:
        print("Ordenados de Mayor a menor:",num2,num3,num1)
elif num3>num1 and num3>num2:
    if num1>num2:
        print("Ordenados de Mayor a menor:",num3,num1,num2)
    else:
        print("Ordenados de Mayor a menor:",num3,num2,num1)

#Ejercicio 30 (Detecta e imprime todos los numeros primos hasta su limite dado por el usuario)
lim=int(input("Escriba un limite de impresion:"))
for i in range(2,lim):
    if i in [2,3,5,7] or (i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0):
        print(i)