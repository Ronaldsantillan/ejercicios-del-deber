
# Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene un aumento del 10% si su
# sueldo es inferior a $600, en caso contrario no tendrá aumento.


class aumento:
 def  __init__ (yo):
     pass
     def  aumento_del_sueldo ( yo ):
        sueldo  =  float ( input ( "ingrese el sueldo:" ))
        if  sueldo  > 600:
            nsueldo  =  sueldo * 0.10
            totalsueldo  =  nsueldo  +  sueldo
            print ( "el nuevo sueldo es de: {}" . formato ( totalsueldo ))
        else:
            sueldo  =  sueldo
            print ( "el sueldo es de: {}" . formato ( sueldo ))

Aumento=aumento()
Aumento.aumento_del_sueldo()