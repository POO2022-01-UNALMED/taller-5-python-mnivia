from zooAnimales.animal import Animal


class Mamifero(Animal):

    _listado=[]
    caballos=0
    leones=0

    def __init__(self,nombre,edad,habitat,genero,pelaje,patas):
        super().__init__(nombre,edad,habitat,genero)
        self._pelaje=pelaje
        self._patas=patas
        Mamifero._listado.append(self)

    def setPelaje(self,pelaje):
          self._pelaje=pelaje

    def getPelaje(self):
          return self._pelaje

    def setPelaje(self,patas):
          self._patas=patas

    def isPelaje(self):
          return self._patas

    def crearCaballo(nombre,edad,genero):
        Mamifero.caballos+=1
        Mamifero._listado.append(Mamifero(nombre,edad,"pradera",genero,True,4))        

    def crearLeon(nombre,edad,genero):
        Mamifero.leones+=1
        Mamifero._listado.append(Mamifero(nombre,edad,"selva",genero,True,4))        
              
    def cantidadMamiferos(self):
        return len(Mamifero._listado)     
