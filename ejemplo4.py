# Dado como dato la calificación de un alumno en un examen, escriba “aprobado” si su calificación
# es mayor o igual que 7 y “Reprobado” en caso contrario.

class Alumno:
    def __init__(self):
        pass
    def calificacion_del_alumno(self):
        cali1 = float(input("ingrese primera calificación:"))
        cali2 = float(input("ingrese segunda calificación:"))
        cali3 = float(input("ingrese tercera calificación:"))
        promedio = (cali1+cali2+cali3)/3
        if promedio >=7 :
            print("Aprobado")
        else:
            print("No aprobó")

        print("la primera calificaión es de:{} la segunda calificación es de:{} la tercera calificación es de:{} el promedio es de:{}".format(cali1,cali2,cali3,promedio)) 

alumno=Alumno()
alumno.calificacion_del_alumno()