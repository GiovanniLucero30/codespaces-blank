# Mensaje de bienvenida
print("¡Bienvenido al programa! Ingresa números para saber si son pares o impares.")
print("Escribe 'salir' para terminar.")

while True:
    # Solicitar al usuario un número o la palabra 'salir'
    entrada = input("Introduce un número (o escribe 'salir' para terminar): ")
    
    # Verificar si el usuario quiere salir
    if entrada.lower() == "salir": # .lower() es un método de las cadenas que convierte toda la cadena sprt a minúsculas
        print("¡Hasta luego! Has salido del programa.")
        break  # Termina el bucle si se ingresa 'salir'
    
    # Intentar convertir la entrada a un número entero
    try:
        numero = int(entrada)
        
        # Determinar si es par o impar
        if numero % 2 == 0:
            print("El número es par.")
        else:
            print("El número es impar.")
    except ValueError:
        print("Por favor, ingresa un número válido o escribe 'salir' para terminar.")
