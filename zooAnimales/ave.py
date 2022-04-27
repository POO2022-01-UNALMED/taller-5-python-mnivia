from zooAnimales.animal import Animal


class Ave(Animal):

    _listado=[]
    _halcones=0
    _aguilas=0

    def __init__(self,nombre,edad,habitat,genero,colorPlumas):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPlumas=colorPlumas        
        Ave._listado.append(self)

    def setColorPlumas(self,colorPlumas):
          self._colorPlumas=colorPlumas

    def getColorPlumas(self):
          return self._colorPlumas

    def crearHalcon(nombre,edad,genero):
        Ave._halcones+=1
        Ave._listado.append(Ave(nombre,edad,"montanas",genero,"cafe glorioso"))                

    def crearAguilas(nombre,edad,genero):
        Ave._aguilas+=1
        Ave._listado.append(Ave(nombre,edad,"montanas",genero,"blanco y amarillo"))
              
    def cantidadAves(self):
        return len(Ave._listado) 

