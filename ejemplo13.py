class Superficie:
    def __int__(self):
        pass
    def calcular_la_superficie_deñ_circulo(self):
        pi=3.1416
        radio = float(input("Ingrese el radio: "))
        a = pi*(radio*radio)
        print("el radio del circulo es: {} la Superficie es: {}".format(radio,a))

superficie=Superficie()
superficie.calcular_la_superficie_deñ_circulo()    