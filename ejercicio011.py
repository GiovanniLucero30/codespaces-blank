# iput para ingresar numeros 
entrada = input("Introduce una lista de números separados por comas (EJ: 3, 5, 7, 2): ")

# Convertir la entrada en una lista de números
numeros = [int(x) for x in entrada.split(",")]

# Inicializar la variable suma
suma_total = 0 # declaramos que suma_total es = a 0 

# Sumar cada con un bucle for
for numero in numeros:
    suma_total += numero # oeracion de suma +=

# Imprime
print(f"La suma de los elementos es: {suma_total}")
