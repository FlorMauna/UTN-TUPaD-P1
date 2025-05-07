#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

lista_multiplos_4 = []

for numero in range (1, 101):
    if numero % 4 == 0:
        lista_multiplos_4.append(numero)

print(lista_multiplos_4)

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
# penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
# indexing con números negativos!

Videojuegos = ["Zelda", "Minecraft", "Assassin's Creed", "God of War", "Hollow Knight"]
print("El penúltimo videojuego de la lista es: ", Videojuegos[-2])

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
# pantalla.

lista_vacia = []
lista_vacia.append("Gomitas")
lista_vacia.append("Caramelos")
lista_vacia.append("Alfajores")
print("Tus golosinas favoritas son las siguientes:", lista_vacia)

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente. Imprimir la lista resultante por pantalla.

animales = ["perro", "gato", "conejo", "tortuga"]
animales[1] = "loro"
animales[-1] = "oso"

print("Mis animales favoritos son: ", animales)

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

numeros = [8, 15, 3, 22, 7] # Se crea una lista de números con los valores de 8, 15, 3, 22 y 7
numeros.remove(max(numeros)) # Acá se busca el valor máximo de la lista anterior y se elimina de la lista
print(numeros) # Se imprime una lista sin el número máxímo (es decir, 22) por lo cual la lista quedaría [8, 15, 3, 7]

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros

numeros = list(range(10, 31, 5))
print("La lista completa de números es: ", numeros)
print("Los dos últimos números son: ", numeros[0], "y", numeros[1])

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# cualesquiera. autos = ["sedan", "polo", "suran", "gol"]

autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "fiat"
autos[2] = "palio"

print(autos)

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla.

dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
# diferentes clientes: compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)

# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)



