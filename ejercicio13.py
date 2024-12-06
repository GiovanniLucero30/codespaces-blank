# iniciar variables notal como lista 
notas = []
print("Ingresa las notas una por una (de 2.0 a 7.0). Escribe 'salir' para terminar.")

while True:
    entrada = input("Nota: ")
    
    # Verificar si el usuario escribió "fin"
    if entrada.strip().lower() == "salir":
        break   # para finalizar la ejecución 
    
    # Intentar convertir la entrada en un número
    try:
        nota = float(entrada) # float toma los decimales
        
        # Validar que la nota esté en el rango permitido agrege un escala de puntuacion del 2 al 7 si estos no son agregados 
        if 2.0 <= nota <= 7.0: # correctamente else impime nota y ecexptvalueerror impime nota para salir dos condiciones. 
            notas.append(nota) # recordar que .append() agrega x a la lista de variable en este caso nota
        else:
            print("La nota debe estar entre 2.0 y 7.0. Inténtalo de nuevo.")
    except ValueError:
        print("Por favor, introduce una nota válida o escribe 'fin' para terminar.")

# Calcular el promedio si hay notas ingresadas
if notas:
    promedio = sum(notas) / len(notas)
    print(f"\nEl promedio es: {promedio:.1f}") # El promedio se imprime con solo un decimal gracias a :.1f si son dos decimales seria :2.f 
    
    # Evaluar si aprobó o reprobó
    if promedio >= 4.0:
        print("¡Aprobaste!")
    else:
        print("Reprobaste.")
else:
    print("\nNo se ingresaron notas.") # imprimir el resultado
