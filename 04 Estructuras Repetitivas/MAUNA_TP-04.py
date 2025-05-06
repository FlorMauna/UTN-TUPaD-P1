#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for numero in range(0,101):
    print(numero)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

numero=int(input("Ingresa un número entero: "))
if numero < 0:
   numero = -numero
contador = 0
while numero > 0:
      numero = numero // 10
      contador = contador + 1
if contador == 0:
    contador = 1
print("El número tiene", contador, "dígito/s.")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

inicio= int(input("Ingresa un primer número: "))
fin = int(input("Ingresa un segundo número: "))
if inicio > fin:
    temp = inicio
    inicio = fin
    fin = temp
suma = 0
for numero in range(inicio +1, fin):
    suma = suma + numero
print("La suma de los números entre", inicio, "y", fin, "es", suma)

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

suma = 0
numero = int(input("Introduce un número entero (escriba 0 para terminar): "))
while numero != 0:
    suma = suma + numero
    numero = int(input("Ingresa otro número entero (escriba 0 para terminar): "))
print("La suma total de los números ingresados es: ", suma)

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número

import random 
numero_secreto = random.randint(0, 9)
intento = -1
contador_intentos = 0
while intento != numero_secreto:
      intento = int(input("Adiviná el número secreto (pista: está entre el 0 y el 9): "))
      contador_intentos = contador_intentos + 1
print("¡Muy bien, el número era", numero_secreto)
print("Lo intentaste:", contador_intentos, "veces")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente

numero = 100
while numero >= 0:
    if numero % 2 == 0:
        print(numero)
    numero = numero - 1

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

entero_pos = int(input("Introduce un número entero que sea positivo por favor: "))
if entero_pos >= 0:
    suma = 0
    numero = 0
    while numero <= entero_pos:
          suma = suma + numero
          numero = numero + 1

    print("La suma de los números de 0 hasta", entero_pos, "es:", suma)
else:
     print("Tenés que introducir un entero positivo, no negativo. Intentalo de nuevo.")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

total_numeros = 100
pares = 0
impares = 0
positivos = 0
negativos = 0

print("Introduce números enteros (escribí 9999 para terminar):")

numero = int(input("Número: "))
while numero != 9999:

    if numero % 2 == 0:
       pares = pares + 1
    else:
        impares + 1

    if numero > 0:
        positivos = positivos + 1
    elif numero < 0:
        negativos = negativos + 1

    numero = int(input("Número: "))

    print("/nResumen:")
    print("Números pares:", pares)
    print("Números impares:", impares)
    print("Números positivos:", positivos)
    print("Números negativos:", negativos)

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor)

suma = 0
cantidad = 0

print("Introduce números enteros para calcular la media (escribi 8888 para terminar):")
numero = int(input("Número: "))

while numero != 8888:
    suma = suma + numero
    cantidad = cantidad + 1
    numero = int(input("Número: "))

if cantidad > 0:
   media = suma / cantidad
   print("Media de los", cantidad, "número/s ingresado/s:", media)
else:
    print("No se ingresaron números.")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = int(input("Ingresá un número entero positivo, por favor: "))

if numero > 0:
    numero_invertido = 0
    
    while numero > 0:
        digito = numero % 10
        numero_invertido = numero_invertido * 10 + digito
        numero = numero // 10 

    print("Número invertido:", numero_invertido)
else:
    print("Por favor, ingresá un número entero positivo mayor que 0.")