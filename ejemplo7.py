#Leer tres números enteros diferentes entre sí y determinar el número mayor de los tres.

class numero:
    
    n1=int(input("ingrese primer numero: "))
    n2=int(input("ingrese segundo numero: "))
    n3=int(input("ingrese tercer numero: "))
    
    if(n1>n2) and (n1>n3):
         print("numero mayor es :", n1)
    else:
        if(n2>n3):
           print("numero mayor es :", n2)
        else:
            print("numero mayor es: ", n3)
       
    



