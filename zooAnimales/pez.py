from zooAnimales.animal import Animal


class Pez(Animal):

    _listado=[]
    _bacalaos=0
    _salmones=0

    def __init__(self,nombre,edad,habitat,genero,zona,colorEscamas,cantidaAletas):
        super().__init__(nombre,edad,habitat,genero,zona)
        self._colorEscamas=colorEscamas        
        self._cantidaAletas=cantidaAletas   
        Pez._listado.append(self)

    def setcolorEscamas(self,colorEscamas):
          self.colorEscamas=colorEscamas

    def getcolorEscamas(self):
          return self._colorEscamas

    def setcantidaAletas(self,cantidaAletas):
          self.cantidaAletas=cantidaAletas

    def getcantidaAletas(self):
          return self.cantidaAletas

    def crearBacalao(nombre,edad,genero,zona):
        Pez._bacalaos+=1
        Pez._listado.append(Pez(nombre,edad,"oceano",genero,zona,"gris",6))                

    def crearSalmon(nombre,edad,genero,zona):
        Pez._salmones+=1
        Pez._listado.append(Pez(nombre,edad,"oceano",genero,zona,"rojo",6))   

    def cantidadPeces(self):
        return len(Pez._listado)
              