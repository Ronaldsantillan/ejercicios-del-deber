# Una escuela aplica dos exámenes a sus aspirantes, por lo que cada uno de ellos 
# obtiene dos calificaciones denotadas como C1 y C2. El aspirante que obtenga 
# calificaciones mayores que 80 en ambos exámenes es aceptado; en caso contrario es rechazado.



class operador:
    c1=float(input("ingrse calificacion1: "))
    c2=float(input("ingrse calificacion2: "))
    if (c1>=80) and (c2>=80):
           print("usted ha sido aceptado")
    else:
          print("usted ha sido rechazado")
          
Operador=operador()