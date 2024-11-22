#from concentrado import Concentrado

class Perro:
    def __init__(self, nombre:str, raza:str, peso:float, edad:int):
        self.__nombre = nombre
        self.__raza=raza
        self.__peso=peso
        self.__edad=edad
        #self.__concentrado = concentrado_perro    
        
    def modificar_nombre(self,nuevo_nombre):
        self.__nombre=nuevo_nombre
        
    def modificar_raza(self,nueva_raza):
        self.__raza=nueva_raza
        
    def modificar_peso(self,nuevo_peso):
        self.__peso=nuevo_peso
        
    def modificar_edad(self,nueva_edad):
        self.__edad=nueva_edad
        
    def dar_nombre(self):
        return self.__nombre
            
    def dar_raza(self):
        return self.__raza
        
    def dar_peso(self):
        return self.__peso
        
    def dar_edad(self):
        return self.__edad
    
    def dar_informacion(self):
        return self.__nombre + "(" + self.__raza +") "+str(self.__peso) + " - " +str(self.__edad)