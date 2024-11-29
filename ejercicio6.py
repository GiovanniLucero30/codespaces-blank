#promedio de 3 numeros

#recordar retur para declarar numeros en global.

def introducir_numeros ():
   global numero1, numero2, numero3
   numero1 =float(input("Introduzca el primer numero: "))
   numero2 =float(input("introduzca el segundo numero: "))
   numero3 =float(input("introduzca el tercer numero: "))
   return numero1, numero2, numero3

# funcion para calcular promedio
def promedio (a, b, c):
  return (a + b + c) / 3 

#llamar a la funcion para introducir los numeros
print("Bienvenido: ")
numero1, numero2, numero3 = introducir_numeros() 

#el resultado
pr = promedio (numero1, numero2, numero3)
print(f"el promedio de los 3 numeros es: {pr}")