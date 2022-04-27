

class Zoologico:  

    def __init__(self,nombre,ubicacion):
        self._nombre=nombre
        self._ubicacion=ubicacion
        self._zonas=[]
        

    def cantidadTotalAnimales(self):
        can=0
        for zona in self._zonas:
            can += zona._animales.cantidadAnimales()
        return can

    def agregarZonas(self,zona):
        self._zonas.append(zona)



