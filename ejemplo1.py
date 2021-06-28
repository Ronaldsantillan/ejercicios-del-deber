# En una tienda se ofrece un descuento del 15% sobre el total de la compra y un cliente desea
# saber cuánto deberá pagar finalmente por su compra.

class descuento:
    def  __init__ ( yo ):
        pass
    def  calcular_el_descuento_ ( self ):
        des  =  float ( input ( "ingrese el descuento:" ))
        compra  =  float ( input ( "ingrese total de la compra:" ))
        total  =  compra * ( des / 100 )
        destotal = compra - total
        print ( "el descuento es del: {}%"   "el total de la compra es: {} lo que debe pagar es: $ {}" . format ( des , compra , destotal ))
Descuento = descuento()
Descuento.calcular_el_descuento_()    




