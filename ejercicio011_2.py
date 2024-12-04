# Inicializar variables
suma_total = 0

print("Introduce números uno por uno y presiona Enter. Escribe 'OK' para terminar:")

# Bucle para pedir números
while True: # Permite que el usuario siga ingresando números hasta que decida detenerse
    entrada = input("Número: ")
    
    # Verificar si el usuario escribió "OK"
    if entrada.strip().lower() == "ok": # Entrada.strip().lower() Convierte la entrada a minúsculas y elimina espacios, para aceptar "OK", " ok " o cualquier variación de ok
        break
    
    # Intentar convertir la entrada en un número y sumarla
    # Try excep valueerror = entradas no válidas y pide al usuario que reingrese un número
    try:
        numero = float(entrada)  # Usamos float para permitir decimales y numeros enteros
        suma_total += numero # esta operacion es una forma más eficiente
    except ValueError: 
        print("Por favor, introduce un número válido o 'OK' para terminar.")

# Imprimir el resultado
print(f"La suma de los números es: {suma_total}")
