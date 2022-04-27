from zooAnimales.animal import Animal


class Reptil(Animal):

    _listado=[]
    _serpientes=0
    _iguanas=0

    def __init__(self,nombre,edad,habitat,genero,zona,colorEscamas,largoCola):
        super().__init__(nombre,edad,habitat,genero,zona)
        self._colorEscamas=colorEscamas        
        self._largoCola=largoCola   
        Reptil._listado.append(self)

    def setcolorEscamas(self,colorEscamas):
          self.colorEscamas=colorEscamas

    def getcolorEscamas(self):
          return self._colorEscamas

    def setlargoCola(self,largoCola):
          self.largoCola=largoCola

    def getlargoCola(self):
          return self._largoCola

    def crearIguana(nombre,edad,genero,zona):
        Reptil._serpientes+=1
        Reptil._listado.append(Reptil(nombre,edad,"humedal",genero,zona,"verde",3))                

    def crearSerpiente(nombre,edad,genero,zona):
        Reptil._iguanas+=1
        Reptil._listado.append(Reptil(nombre,edad,"jungla",genero,zona,"blanco",1))

    def cantidadReptiels(self):
        return len(Reptil._listado)                        
              