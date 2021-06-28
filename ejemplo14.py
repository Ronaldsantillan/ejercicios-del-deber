# Calcular el factorial de N números enteros leídos de teclado.
# El problema consistirá en realizar una estructura de N iteraciones aplicando el factorial de un número.

class Tarea:
    def factorial(self):
        n=int(input("ingrese la cantidad de numeros: "))
        for i in range(n):
            numero= int(input("ingrese n numero: "))
            acu=1
            for num in range(numero,1,-1):
              acu = acu*num
            print("numero:={},factorial:={}".format(numero,acu))  
        
tarea = Tarea()
tarea.factorial()
            
        
        
    