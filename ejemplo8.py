# Diseñar un algoritmo tal que dados como datos dos variables de tipo entero
# obtenga el resultado de la siguiente función

class dados:
    def __init__(self):
        pass
    def switch(self):
        respuesta=0
        num = int(input("ingrese el numero:"))
        v = int(input("ingrese variable:"))
        if num == 1:
            respuesta = 100*v
        elif num == 2:
            respuesta = 100**v
        elif num == 3:
            respuesta = 100/v
        else :
            respuesta = 0
        print("la respuesta es:{} el valor es: {} el valor de la variable es: {}".format(respuesta,v,num))

Datos=dados()
Datos.switch()