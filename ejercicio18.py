# Clasificacion de edades niño, adolecente, adulto 

# 1.- El usuario inicia seleccionando una opción desde el menú (clasificar edades o salir).
# Definimos el menu que vamos a utilizar para tener mejor interaccion en la terminal 
# este meno lo declararemos al final.

def Rango_de_edad():
    """Clasifica edades en niño, adolescente, adulto o adulto mayor.""" # nota de accion a realizar!
    # El programa comienza con una serie de mensajes para dar
    # la bienvenida al usuario y ofrecer un menú de opciones. Este menú le permite al usuario el
    # Estas líneas muestran el texto que se muestra al usuario en la pantalla. Aquí es donde el usuario recibe las opciones del menú.
    while True: # Iniciamos el bucle While True
        print("\nBienvenido al clasificador de edades. ¿Qué te gustaría hacer hoy?" # Utilizo """""""" para ahorra tiempo en el menu 
              "1. Clasificar edades"                                                # utilizando demaciados print.
              "2. Salir"""
        ) # recuerda cerrar el print 

        try: #  El bloque try intención except captura el input
            opcion = int(input("Selecciona una opción (1 o 2): ")) # Verificación de Opción y Continuación del Programa
            if opcion == 1: 
                break
            elif opcion == 2:
                print("¡Gracias por usar el programa! Hasta luego.")
                return # return: Si elige la opción 2, el programa imprime un mensaje de despedida y termina.
            else:
                print("Opción no válida. Por favor, ingresa 1 o 2.") # mesaje de error 
                continue
        except ValueError:
            print("Por favor, ingresa un número válido (1 o 2).")
            continue

    # Bucle principal para clasificar edades
    while True:
        try:
            total_edades = int(input("¿Cuántas edades deseas clasificar? (Escribe un número mayor a 0): "))
            if total_edades <= 0:
                print("Por favor, ingresa un número mayor a 0.") # mensaje de error
                continue
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")
            continue

        # Contadores para las categorías
        ninos = 0
        adolescentes = 0
        adultos = 0
        adultos_mayores = 0

        # Procesar edades
        for i in range(total_edades):
            try:
                edad = int(input(f"Ingrese la edad #{i + 1}: "))

                # Verificar que la edad esté dentro de un rango razonable
                if edad < 0:
                    print("¡La edad no puede ser negativa! Por favor, ingresa una edad válida.")
                    continue
                elif edad > 120:
                    print("¡Esa edad es irreal! Ingresa una edad menor o igual a 120 años.")
                    continue
                
                if edad < 13:
                    print("Categoría: Niño")
                    ninos += 1
                elif 13 <= edad <= 17:
                    print("Categoría: Adolescente")
                    adolescentes += 1
                elif 18 <= edad <= 59:
                    print("Categoría: Adulto")
                    adultos += 1
                else:  # edad >= 60
                    print("Categoría: Adulto mayor")
                    adultos_mayores += 1
            except ValueError:
                print("Por favor, ingresa una edad válida.")
                continue

        # Mostrar resumen
        print("\nResumen de clasificación:")
        print(f"Niños: {ninos}")
        print(f"Adolescentes: {adolescentes}")
        print(f"Adultos: {adultos}")
        print(f"Adultos mayores: {adultos_mayores}")

        # Preguntar si se desea continuar
        continuar = input("\n¿Quieres clasificar más edades? (si / no): ").strip().lower()
        if continuar == "no":
            print("¡Gracias por usar el programa! Hasta luego.")
            break

# Ejecutar el programa
Rango_de_edad()
