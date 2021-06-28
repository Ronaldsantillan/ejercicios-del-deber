# Determinar la cantidad de dinero que recibirá un trabajador por concepto de 
# las horas extras trabajadas en una empresa, sabiendo que cuando las horas de 
# trabajo exceden de 40, el resto  se consideran horas extras y que éstas se pagan 
# al doble de una hora normal cuando no exceden de 8;  si las horas extras exceden de 8 
# se pagan las primeras 8 al  doble de lo que se paga por una hora normal y el resto al triple

class Tarea:
    def __init__(self):
        pass
    def calcularjornada(self):
         ht, he, het=0,0,0
         ph, phe, pt,ph8=0,0,0,0
         ht= int(input("ingrese horas trabajadas: "))
         ph= float(input("ingrese valor hora: "))
         if ht > 40:
             he = ht - 40
             if he > 8:
                het = he - 8
                ph8 = 8*ph*2
                phe = het*ph*3
             else:
                phe = 0
                ph8 = he*ph*2
             pt = 40*ph + ph8 + phe 
         else:
             pt =ht*ph
         print("sobretiempo<8:{} sobretiempo>8:{} jornada:{} ".format(ph8,phe,pt))  
               
tarea = Tarea()
tarea.calcularjornada()           
                         