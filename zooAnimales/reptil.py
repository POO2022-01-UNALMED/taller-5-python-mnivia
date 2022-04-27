from zooAnimales.animal import Animal


class Reptil(Animal):

    _listado=[]
    serpientes=0
    iguanas=0

    def __init__(self,nombre=None,edad=None,habitat=None,genero=None,colorEscamas=None,largoCola=None):
        super().__init__(nombre,edad,habitat,genero)
        self._colorEscamas=colorEscamas        
        self._largoCola=largoCola   
        Reptil._listado.append(self)

    def setColorEscamas(self,colorEscamas):
          self.colorEscamas=colorEscamas

    def getColorEscamas(self):
          return self._colorEscamas

    def setLargoCola(self,largoCola):
          self.largoCola=largoCola

    def getLargoCola(self):
          return self._largoCola

    def crearIguana(nombre,edad,genero):
        Reptil.iguanas+=1
        Reptil(nombre,edad,"humedal",genero,"verde",3)

    def crearSerpiente(nombre,edad,genero):        
        Reptil.serpientes+=1
        Reptil(nombre,edad,"jungla",genero,"blanco",1)

    @classmethod
    def cantidadReptiels(cls):
        return len(cls._listado)                        