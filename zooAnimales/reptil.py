from zooAnimales.animal import Animal


class Reptil(Animal):

    _listado=[]
    _serpientes=0
    _iguanas=0

    def __init__(self,nombre,edad,habitat,genero,colorEscamas,largoCola):
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
        Reptil._serpientes+=1
        Reptil._listado.append(Reptil(nombre,edad,"humedal",genero,"verde",3))                

    def crearSerpiente(nombre,edad,genero):
        Reptil._iguanas+=1
        Reptil._listado.append(Reptil(nombre,edad,"jungla",genero,"blanco",1))

    def cantidadReptiels(self):
        return len(Reptil._listado)                        
              