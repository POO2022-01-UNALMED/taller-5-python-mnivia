from zooAnimales.animal import Animal


class Ave(Animal):

    _listado=[]
    _halcones=0
    _aguilas=0

    def __init__(self,nombre,edad,habitat,genero,zona,colorPlumas):
        super().__init__(nombre,edad,habitat,genero,zona)
        self._colorPlumas=colorPlumas        
        Ave._listado.append(self)

    def setcolorPlumas(self,colorPlumas):
          self._colorPlumas=colorPlumas

    def getcolorPlumas(self):
          return self._colorPlumas

    def crearHalcon(nombre,edad,genero,zona):
        Ave._halcones+=1
        Ave._listado.append(Ave(nombre,edad,"montanas",genero,zona,"cafe glorioso"))                

    def crearAguilas(nombre,edad,genero,zona):
        Ave._aguilas+=1
        Ave._listado.append(Ave(nombre,edad,"montanas",genero,zona,"blanco y amarillo"))
              
    def cantidadAves(self):
        return len(Ave._listado) 

