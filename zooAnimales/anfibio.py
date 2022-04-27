from zooAnimales.animal import Animal

class Anfibio(Animal):

    _listado=[]
    _salamandras=0
    _ranas=0

    def __init__(self,nombre,edad,habitat,genero,zona,colorPiel,venenoso):
        super().__init__(nombre,edad,habitat,genero,zona)
        self._colorPiel=colorPiel
        self._venenoso=venenoso
        Anfibio._listado.append(self)

    def setcolorPiel(self,colorPiel):
        self._colorPiel=colorPiel

    def getcolorPiel(self):
        return self._colorPiel

    def setvenenoso(self,venenoso):
        self._venenoso=venenoso

    def getvenenoso(self):
        return self._venenoso


    def crearRana(nombre,edad,genero,zona):
        Anfibio._ranas+=1
        Anfibio._listado.append(Anfibio(nombre,edad,"selva",genero,zona,"rojo",True))                

    def crearSalamandra(nombre,edad,genero,zona):
        Anfibio._salamandras+=1
        Anfibio._listado.append(Anfibio(nombre,edad,"selva",genero,zona,"negro y amarillo",False))

    def cantidadAnfibios(self):
        return len(Anfibio._listado)

              