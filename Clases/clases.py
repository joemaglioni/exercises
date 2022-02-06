import math
class Circulo:
    
    def __init__(self, radio=1):
        self.radio = self._validar_radio(radio)

    def _validar_radio(self, radio):
        if type(radio) != int:
            raise TypeError("Solo se aceptan numeros enteros")
        if radio < 0:
            raise Exception("Un circulo con radio negativo no existe!, solo se lo puede imaginar")
        elif radio == 0:
            raise Exception("Un circulo de radio cero no existe!, solo es un punto")
        return radio

    @property
    def radio(self):
        return self._radio
    
    @radio.setter    
    def radio(self, value):
        if type(value) != int:
            raise TypeError("Solo se aceptan numeros enteros")
        if value < 0:
            raise Exception("Un circulo con radio negativo no existe!, solo se lo puede imaginar")
        elif value == 0:
            raise Exception("Un circulo de radio cero no existe!, solo es un punto")
        self._radio = value

    def area(self):
        """
        Testing area function
        >>> Circulo(radio = 2).area()
        12.566370614359172

        Testing zero number
        >>> Circulo(radio = 0).area()
        Traceback (most recent call last):
        ...
        Exception: Un circulo de radio cero no existe!, solo es un punto
        
        Testing negative number
        >>> Circulo(radio=-1).area()
        Traceback (most recent call last):
        ...
        Exception: Un circulo con radio negativo no existe!, solo se lo puede imaginar

        Testing int number
        >>> Circulo(radio="1").area()
        Traceback (most recent call last):
        ...
        TypeError: Solo se aceptan numeros enteros
        """
        return (math.pi)*(self.radio)**2

    def perimetro(self):
        """
        Testing perimetro function
        >>> Circulo(radio = 2).perimetro()
        12.566370614359172

        Testing zero number
        >>> Circulo(radio = 0).perimetro()
        Traceback (most recent call last):
        ...
        Exception: Un circulo de radio cero no existe!, solo es un punto
        
        Testing negative number
        >>> Circulo(radio=-1).perimetro()
        Traceback (most recent call last):
        ...
        Exception: Un circulo con radio negativo no existe!, solo se lo puede imaginar

        Testing int number
        >>> Circulo(radio="1").perimetro()
        Traceback (most recent call last):
        ...
        TypeError: Solo se aceptan numeros enteros
        """

        return 2*(math.pi)*(self.radio)


    def multiplicar(self,numero):
        """
        Testing multiplicar function
        >>> type(Circulo(radio=1).multiplicar(numero=1))
        <class '__main__.Circulo'>
        
        Testing zero 
        >>> Circulo(radio=1).multiplicar(numero=0)
        Traceback (most recent call last):
        ...
        Exception: Un circulo de radio cero no existe!, solo es un punto

        Testing negative number
        >>> Circulo(radio=1).multiplicar(numero=-1)
        Traceback (most recent call last):
        ...
        Exception: Un circulo con radio negativo no existe!, solo se lo puede imaginar

        Testing int number
        >>> Circulo(radio=1).multiplicar(numero="1")
        Traceback (most recent call last):
        ...
        TypeError: Solo se aceptan numeros enteros
        """

        circulo = Circulo(self.radio*numero)
        return circulo

    def representacion(self):
        for i in range((self.radio*2)+1):
            for j in range((self.radio*2)+1):
                ec = ((j)-self.radio)**2 + ((i)-self.radio)**2
                res = int((self.radio)**2)
                if ((j)-self.radio)**2 + ((i)-self.radio)**2 <= int((self.radio)**2):
                    print("*",end="")
                else:
                    print(" ",end="")
            print(" ")

    def __str__(self):
        self.representacion()
        return "Hola soy un circulo y la longitud de mi radio es "+str(self.radio)




if __name__ == '__main__':
    
    import doctest
    doctest.testmod()