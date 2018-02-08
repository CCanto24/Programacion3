from abc import abstractmethod

class Figura(object):
    def __init__(self, lado=0.0):
        self.lado = lado
    def calcular_area(self,lado):
        area = lado * lado
        return area

class Circulo(Figura):

    def calcular_area(self, lado):
        area = 3.1416*lado
        return area
    def calcular_circunferencia(self,lado):
        circunferencia = 2*3.1416*lado
        return circunferencia

class Cuadrado(Figura):
    def calcular_perimetro(self, lado):
        perimetro = 4*lado
        return perimetro

if __name__ == "__main__":
    radio = float(input("Ingresar radio del circulo: "))
    x = Circulo(radio)
    areaci = x.calcular_area(radio)
    print("El area del circulo de radio: " + str(x.lado) + " es " + str(areaci))
    circunferencia = x.calcular_circunferencia(radio)
    print("La circunferencia del circulo de radio: " + str(x.lado) + " es " + str(circunferencia))
    lado = float(input("Ingrese el valor de un lado del cuadrado: "))
    y = Cuadrado(lado)
    areacu = y.calcular_area(lado)
    print("El area del cuadrado con lados: " + str(y.lado) + " es " + str(areacu))
    perimetro = y.calcular_perimetro(lado)
    print("El perimetro del cuadrado con lados: " + str(y.lado) + " es " + str(perimetro))