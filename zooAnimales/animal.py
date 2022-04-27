

class Animal():

    _totalAnimales=0    

    def __init__(self,nombre=None,edad=None,habitat=None,genero=None):
        self._nombre=nombre
        self._edad=edad
        self._habitat=habitat
        self._genero=genero
        self._zona=None
        Animal._totalAnimales+=1


    def setNombre(self,nombre):
          self._nombre=nombre  

    def getNombre(self):       
          return self._nombre  

    def setEdad(self,edad):    
          self._edad=edad      

    def getEdad(self):
          return self._edad

    def setHabitat(self,habitat):
          self._habitat=habitat

    def getHabitat(self):
          return self._habitat

    def setGenero(self,genero):
          self._genero=genero

    def getGenero(self):
          return self._genero
 
    def setZona(self,zona):
          self._zona=zona

    def getZona(self):
          return self._zon

    def totalPorTipo(self):
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.ave import Ave
        from zooAnimales.reptil import Reptil
        from zooAnimales.pez import Pez
        from zooAnimales.anfibio import Anfibio
        return "Mamiferos: "+ Mamifero.cantidadMamiferos() +"\n"+ "Aves: "+ Ave.cantidadAves() +"\n" + "Reptiles: "+ Reptil.cantidadReptiels() +"\n" + "Peces: "+ Pez.cantidadPeces() +"\n" + "Anfibios: "+ Anfibio.cantidadAnfibios()   

    def toString(self) -> str:
        if (self.getZona()!=None):
            return "Mi nombre es "+ self.getNombre()+", tengo una edad de "+self.getEdad()+ ", habito en "+ self.getHabitat()+ " y mi genero es "+ self.getGenero()+", la zona en la que me ubico es "+ self.zona.getNombre()+", en el" +self.zona.zoo.getNombre()    
        else:
            return "Mi nombre es "+ self.getNombre()+", tengo una edad de "+self.getEdad()+ ", habito en "+ self.getHabitat()+ " y mi genero es "+ self.getGenero()    

        

