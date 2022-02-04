class Circulo:
    
    def __init__(self, radio=1):
        self.radio = self._validar_radio(radio)


    def _validar_radio(self, radio):
        if type(radio) != int:
            raise ValueError("Solo se aceptan numeros enteros")
        if radio < 0:
            raise ValueError("Un circulo con radio negativo no existe!, solo se lo puede imaginar")
        elif radio == 0:
            raise ValueError("Un circulo de radio cero no existe!, solo es un punto")
        return radio

    @property
    def radio(self):
        return self._radio
    
    @radio.setter    
    def radio(self, value):
        if value < 0:
            raise ValueError("Un circulo con radio negativo no existe!, solo se lo puede imaginar")
        elif value == 0:
            raise ValueError("Un circulo de radio cero no existe!, solo es un punto")
        self._radio = value

    def area(self):
        return (math.pi)*(self.radio)**2

    def perimetro(self):
        return 2*(math.pi)*(self.radio)


    def multiplicar(self,numero):
        circulo = Circulo(self.radio*numero)
        return circulo

    def representacion(self):
        for i in range((self.radio*2)+1):
            for j in range((self.radio*2)+1):
                ec = ((j)-self.radio)**2 + ((i)-self.radio)**2
                res = int((self.radio)**2)
                # print("ecuacion", ec)
                # print("Resultado", res)
                if ((j)-self.radio)**2 + ((i)-self.radio)**2 <= int((self.radio)**2):
                    print("*",end="")
                else:
                    print(" ",end="")
            
            print(" ")
        
        

    def __str__(self):
        self.representacion()
        return "Hola soy un circulo y mi radio es de "+str(self.radio)




if __name__ == '__main__':
    c1 = Circulo(3)
    c2 = c1.multiplicar(2)
    c2.radio=2
    print(c2)