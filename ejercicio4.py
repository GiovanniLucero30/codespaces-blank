#Caladora simplimple 
#objetivo realizar una calculadora eficiente.
print("bienvenido a la calculadora COD-17!")
#def: define una funcion como por ejemplo la ejucion de una divicion.
#utilizare def para deficir todas las funciones matematicas.
def introducir_numeros ():
   global numero1, numero2 
   numero1 =float(input("Introduzca el primer numero: "))
   numero2 =float(input("introduzca el segundo numero: "))


#ahora deficimos las funciones de cada variable matematica. 
def sumar (a, b) :
  print("la suma de ",a," + ",b," = ", a+b)

def restar (a,b) :
  print("la resta de ",a," - ",b," = ", a - b)

def multiplicar (a,b) :
  print("la multiplicacion de ",a," * ",b," = ", a * b)

def dividir (a, b):
    if b == 0:
         print("Nose puede dividir entre cero")
    else:
         print("la division de ",a," / ",b," = ", a / b)

#while es un bucle condicional, con condiciones especificas.

while True:
  print("""
     Indique la operacion a realizar:
     
    1- sumar
    2- restar 
    3- multiplicar
    4- dividir
    5- salir""")
  
  eleccion = int(input())

  if eleccion == 1:
    introducir_numeros ()
    sumar (numero1, numero2)
  elif eleccion == 2:
    introducir_numeros ()
    restar (numero1, numero2)
  elif eleccion == 3:
    introducir_numeros ()
    multiplicar (numero1, numero2)
  elif eleccion == 4:
    introducir_numeros ()
    dividir (numero1, numero2)
  elif eleccion == 5:
    print("Adios de nada por ayudarte!")
    break
  
#break Rompe el blucle (lo cierra)


  