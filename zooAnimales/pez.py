from zooAnimales.animal import Animal


class Pez(Animal):

    _listado=[]
    _bacalaos=0
    _salmones=0

    def __init__(self,nombre,edad,habitat,genero,colorEscamas,cantidaAletas):
        super().__init__(nombre,edad,habitat,genero)
        self._colorEscamas=colorEscamas        
        self._cantidaAletas=cantidaAletas   
        Pez._listado.append(self)

    def setColorEscamas(self,colorEscamas):
          self.colorEscamas=colorEscamas

    def getColorEscamas(self):
          return self._colorEscamas

    def setCantidadAletas(self,cantidaAletas):
          self._cantidaAletas=cantidaAletas

    def getCantidadAletas(self):
          return self._cantidaAletas

    def crearBacalao(nombre,edad,genero):
        Pez._bacalaos+=1
        Pez._listado.append(Pez(nombre,edad,"oceano",genero,"gris",6))                

    def crearSalmon(nombre,edad,genero):
        Pez._salmones+=1
        Pez._listado.append(Pez(nombre,edad,"oceano",genero,"rojo",6))   

    def cantidadPeces(self):
        return len(Pez._listado)
              