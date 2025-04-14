#Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”
print("Hola Mundo")

#Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.
nombre = input ("Ingresá tu nombre")
print(f"Hola {nombre}!")

#Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.
nombre = input ("Ingresa tu nombre:")
apellido = input ("Ingresa tu apellido:")
edad = input("Ingresa tu edad:")
residencia = input("Ingresa tu lugar de residencia")
print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro
import math
radio = float(input("Ingresa el radio de un círculo"))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"El área de ese círculo es de {area:.2f} y su perímetro es de {perimetro:.2f}.")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.
segundos = int (input("Ingresa una cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas:.2f}horas.")

#Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
print (f"Tabla de multiplicar del {numero}: ")
print (f"{numero} x 1 = {numero * 1}")
print (f"{numero} x 2 = {numero * 2}")
print (f"{numero} x 3 = {numero * 3}")
print (f"{numero} x 4 = {numero * 4}")
print (f"{numero} x 5 = {numero * 5}")
print (f"{numero} x 6 = {numero * 6}")
print (f"{numero} x 7 = {numero * 7}")
print (f"{numero} x 8 = {numero * 8}")
print (f"{numero} x 9 = {numero * 9}")
print (f"{numero} x 10 = {numero * 10}")

#Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
num1 = int(input("Por favor, ingresa el primer número entero (distinto de 0): "))
num2 = int(input("Por favor, ingresa el segundo número entero (distinto de 0): "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print(f"La suma de {num1} y {num2} es: {suma}")
print(f"La resta de {num1} y {num2} es: {resta}")
print(f"La multiplicación de {num1} y {num2} es: {multiplicacion}")
print(f"La división de {num1} entre {num2} es: {division:.2f}")

#Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo:𝐼𝑀𝐶 =𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2
peso = float(input("Por favor, ingresa tu peso en KG: "))
altura = float(input("Por favor, ingresa tu altura en metros: "))
imc = peso / (altura ** 2)

print(f"Tu índice de masa corporal IMC es: {imc:.2f}")

# Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
celsius = float(input("Por favor, ingresa la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32

print(f"La temperatura en grados Fahrenheit es: {fahrenheit:.2f}")

#Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.
num1 = float(input("Por favor, ingresa el primer número: "))
num2 = float(input("Por favor, ingresa el segundo número: "))
num3 = float(input("Por favor, ingresa el tercer número: "))
promedio = (num1 + num2 + num3) / 3

print(f"El promedio de los tres números es: {promedio:.2f}")
