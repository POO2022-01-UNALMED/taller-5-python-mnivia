from zooAnimales.animal import Animal


class Mamifero(Animal):

    _listado=[]
    _caballos=0
    _leones=0

    def __init__(self,nombre,edad,habitat,genero,zona,pelaje,patas):
        super().__init__(nombre,edad,habitat,genero,zona)
        self._pelaje=pelaje
        self._patas=patas
        Mamifero._listado.append(self)

    def setPelaje(self,pelaje):
          self._pelaje=pelaje

    def getPelaje(self):
          return self._pelaje

    def setPelaje(self,patas):
          self._patas=patas

    def getPelaje(self):
          return self._patas

    def crearCabalo(nombre,edad,genero,zona):
        Mamifero._caballos+=1
        Mamifero._listado.append(Mamifero(nombre,edad,"pradera",genero,zona,True,4))        

    def crearLeon(nombre,edad,genero,zona):
        Mamifero._leones+=1
        Mamifero._listado.append(Mamifero(nombre,edad,"selva",genero,zona,True,4))        
              
    def cantidadMamiferos(self):
        return len(Mamifero._listado)     
