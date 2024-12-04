# Se solicitan los numeros separados por comas
entrada = input("Introduce una lista de números separados por comas (por ejemplo: 1, 2, 3, 4, etc.): ")

# Convertir la entrada en una lista de números pares
numeros = [int(x) for x in entrada.split(",")] # .split(",") y se convierten en enteros con una comprensión de lista y este texto se divide ne lementos

# lista para los números pares
pares = []

# Filtrar con un bucle for
for numero in numeros:
    if numero % 2 == 0:  # Comprobar si el número es par con % 2 = 0
        pares.append(numero) #si esl numero es par se agrega a la lista gracias al comando .append()

# Imprimir: como resultado solo imprime los pares. 
print(f"Números pares: {pares}")
