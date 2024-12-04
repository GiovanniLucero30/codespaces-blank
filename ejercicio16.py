# Iniciar para almacenar la suma
print("¡Bienvenido esta es la suma de pares del 1 al 50: ")

suma_pares = 0 # establecer variable en 0

# Usar un bucle for para sumar rango entre 1 y 50
for i in range(1, 51): # iteración ojo con agregar 1 numer extra (51)
    if i % 2 == 0:  # Verificar si el número es par
        suma_pares += i  # Sumar el número par a la suma

# Imprimir el resultado
print(f"La suma de los números pares entre 1 y 50 es: {suma_pares}")
