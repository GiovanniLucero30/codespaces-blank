print("¡Bienvenido a la calculadora de IVA!")

# Función para introducir el precio del producto
def introducir_numero():
    while True:
        try:
            # Solicitar el valor del producto y convertirlo a float
            valor = float(input("Introduce el valor del producto: "))
            return valor
        except ValueError:
            print("Por favor, ingresa un número válido para el precio del producto.")

# Función para calcular el IVA
def iva(a):
    return a * 0.19

while True:
    print("""
    1 - Ver el Valor con el IVA
    2 - Salir
    """)
    
    try:
        # Solicitar la opción
        eleccion = int(input("Elige una opción (1 o 2): "))

        # Opción 1: Calcular el IVA
        if eleccion == 1:
            numero1 = introducir_numero()  # Llamada a la función para obtener el valor
            iva_calculado = iva(numero1)  # Calcular el IVA
            total = numero1 + iva_calculado  # Calcular el total con IVA
            print(f"Tenemos el resultado!, el total con el IVA es: $ {total}")

        # Opción 2: Salir del bucle
        elif eleccion == 2:
            print("¡Espero verte luego!")
            break  # Salir del bucle

        # Opción no válida
        else:
            print("Opción no válida. Por favor, elige 1 o 2.")

    except ValueError:
        # Manejo de error si el usuario no ingresa un número válido
        print("Por favor, ingresa un número válido (1 o 2).")
    break