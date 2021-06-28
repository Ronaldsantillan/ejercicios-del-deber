#  Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas.
#  El vendedor desea saber cuánto dinero obtendrá por concepto de comisiones
#  por las tres ventas que realizaen el mes y el total que recibirá 
#  en el mes tomando en cuenta su sueldo base y sus comisiones.

class comisión:
     def  __init__ ( sel ):
        pass
     def  calcular_comisión ( self ):
        descuento = float ( input ( "ingrese el porcentaje del descuento:" ))
        venta1  =  float ( input ( "ingrese el valor de la primera venta:" ))
        venta2  =  float ( input ( "ingrese el valor de la segunda venta:" ))
        venta3  =  float ( input ( "ingrese el valor de la tercera venta:" ))
        sueldo_base  =  float ( input ( "ingrse el sueldo base:" ))
        Total_de_las_ventas  =  venta1 + venta2 + venta3
        comision  =  Total_de_las_ventas * ( descuento / 100 )
        total_a_recibir  =  sueldo_base + comision
        print ( "el valor de la primera venta es: {} el valor de la segunda venta es: {} el valor de la tercera venta es: {} el total de las ventas es: {} el valor de la comsision es: { } el total a recibir es de: {} " . formato ( venta1 , venta2 , venta3 , Total_de_las_ventas , comision , total_a_recibir ))

Comisión = comisión()
Comisión.calcular_comisión()