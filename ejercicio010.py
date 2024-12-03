# imprimir mensaje de entrada
print("Generador de listas numéricas. Escribe un número para generar la lista, o 'salir' para terminar.")
# valor condicional While
while True:
    # Solicitar entrada del usuario
    entrada = input("Introduce un número entero o escribe 'salir' para finalizar: ")
    
    # Verificar si el usuario desea salir
    if entrada.lower() == "salir": # Si? entrada.lower() == al texto salir
        print("¡Hasta luego!") #imprime
        break # Define el final del bucle 

    # convertir la entrada en numero entero with try
    try:
        n = int(entrada)
        # Inicializar la lista y el contador
        numeros = []
        contador = 1 # valor contador comienza en 1
        
        # Generar la lista de números del 1 al n
        while contador <= n:
            numeros.append(contador) # numero de apertura
            contador += 1
        
        # Mostrar la lista generada
        print("Lista generada:", numeros)
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número entero o 'salir'.")
