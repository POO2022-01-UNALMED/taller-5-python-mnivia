

class Zoologico:  

    def __init__(self,nombre,ubicacion):
        self._nombre=nombre
        self._ubicacion=ubicacion
        self._zona=[]
        
    def setNombre(self,nombre):
          self._nombre=nombre

    def getNombre(self):
          return self._nombre

    def setUbicacion(self,ubicacion):
          self._ubicacion=ubicacion

    def getUbicacion(self):
          return self._ubicacion    

    def setZona(self,zona):
          self._zona=zona

    def getZona(self):
          return self._zona              

    def cantidadTotalAnimales(self):
        can=0
        for zona in self._zona:
            can += zona.cantidadAnimales()
        return can

    def agregarZonas(self,zona):
        self._zona.append(zona)



