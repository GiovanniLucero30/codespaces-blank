# Solicitar al usuario que ingrese cantidad de horas, minutos y segundos.
print("bienvenido usuario igrsese su tiempo de code: ")
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))
# Calcular el tiempo total.
total_segundos = (horas * 3600) + (minutos * 60) + segundos
# imprime el resultado.
print(f"El tiempo total es: {total_segundos} segundos")