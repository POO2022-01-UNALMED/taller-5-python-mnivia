from zooAnimales.animal import Animal

class Anfibio(Animal):

    _listado=[]
    salamandras=0
    ranas=0

    def __init__(self,nombre=None,edad=None,habitat=None,genero=None,colorPiel=None,venenoso=None):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPiel=colorPiel
        self._venenoso=venenoso
        Anfibio._listado.append(self)

    def setcolorPiel(self,colorPiel):
        self._colorPiel=colorPiel

    def getColorPiel(self):
        return self._colorPiel

    def setvenenoso(self,venenoso):
        self._venenoso=venenoso

    def isVenenoso(self):
        return self._venenoso


    def crearRana(nombre,edad,genero):
        Anfibio.ranas+=1
        Anfibio._listado.append(Anfibio(nombre,edad,"selva",genero,"rojo",True))                

    def crearSalamandra(nombre,edad,genero):
        Anfibio.salamandras+=1
        Anfibio._listado.append(Anfibio(nombre,edad,"selva",genero,"negro y amarillo",False))

    def cantidadAnfibios(self):
        return len(Anfibio._listado)

              