#Calcular la suma de los cuadrados de los primeros 100 enteros y escribir el resultado.

class forrepeticion:
    def __init__(self):
        pass
    def ciclo_for(self):
        suma,n,i=0,0,0
        for i in range(100):
            suma=suma+i*i
            print ("el contador es:{} la suma es:{}".format(i,suma))
For=forrepeticion()
For.ciclo_for()



