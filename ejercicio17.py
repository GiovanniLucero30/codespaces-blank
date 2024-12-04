import random

# Generar un número aleatorio entre 1 y 20
numero_aleatorio = random.randint(1, 20)

# Mensaje de bienvenida
print("Bienvenido al juego de adivinanza.")
print("He elegido un número entre 1 y 20. ¡Intenta adivinarlo!")

# Iniciar el bucle while
while True:
    # Pedir al usuario que ingrese un número
    intento = int(input("Ingresa tu número: "))

    # Comprobar si el número ingresado es el correcto
    if intento < numero_aleatorio:
        print("Pista: El número es mayor.")
    elif intento > numero_aleatorio:
        print("Pista: El número es menor.")
    else:
        print(f"¡Felicidades! Adivinaste el número, que era {numero_aleatorio}.")
        break  # Salir del bucle cuando el número es adivinado
