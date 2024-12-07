# Calculadora de areas
# Definir las funciones para calcular áreas

def area_cuadrado(un_lado):
    """Calcula el área de un cuadrado dado un lado."""
    return un_lado ** 2

def area_rectangulo(base, altura):
    """Calcula el área de un rectángulo dada su base y altura."""
    return base * altura

def area_triangulo(base, altura):
    """Calcula el área de un triángulo dada su base y altura."""
    return (base * altura) / 2

# Definir el menú
def menu():
    print("¡Bienvenido a la calculadora de áreas!")
    print("Aquí podrás calcular el área de 3 figuras geométricas.")

    while True:
        print("""
        Ingresa una opción válida [1, 2, 3, 4]:
        1.- Calcular el área de un cuadrado
        2.- Calcular el área de un rectángulo
        3.- Calcular el área de un triángulo
        4.- Salir
        """)

        opcion = input("Elige una opción: ")  # Elegir opción del menú

        if opcion in ["1", "2", "3", "4"]:
            if opcion == "1":
                # Área del cuadrado
                try:
                    un_lado = float(input("Ingresa el valor de un lado del cuadrado: "))
                    area = area_cuadrado(un_lado)
                    print(f"El área del cuadrado es: {area:.2f} cm²")
                except ValueError:
                    print("Por favor, ingresa un número válido.")

            elif opcion == "2":
                # Área del rectángulo
                try:
                    base = float(input("Ingresa la base del rectángulo: "))
                    altura = float(input("Ingresa la altura del rectángulo: "))
                    area = area_rectangulo(base, altura)
                    print(f"El área del rectángulo es: {area:.2f} cm²")
                except ValueError:
                    print("Por favor, ingresa un número válido.")

            elif opcion == "3":
                # Área del triángulo
                try:
                    base = float(input("Ingresa la base del triángulo: "))
                    altura = float(input("Ingresa la altura del triángulo: "))
                    area = area_triangulo(base, altura)
                    print(f"El área del triángulo es: {area:.2f} cm²")
                except ValueError:
                    print("Por favor, ingresa un número válido.")

            elif opcion == "4":
                # Salir del programa
                print("\n¡Gracias por usar el programa! ¡Hasta la próxima!")
                break
        else:
            print("Opción inválida. Intenta de nuevo.")  # Opción no válida

# Ejecutar el programa
if __name__ == "__main__":
    menu()
