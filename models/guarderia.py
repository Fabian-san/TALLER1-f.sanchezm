from models.perro import Perro
#from concentrado import Concentrado

class Guarderia:
    def __init__(self,nombre:str,ubicacion:str,perros:list):
        self._nombre= nombre
        self._ubicacion=ubicacion
        self._perros=perros
        #self.__concentrados=concentrados
        
    def retornar_perros(self)->tuple[Perro]:
        return tuple(self._perros)
    
    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value:str) -> None:

        if isinstance(value, str):
            self._nombre = value
        else:
            raise ValueError('Expected str')
    @property
    def ubicacion(self) -> str:
        return self._ubicacion

    @ubicacion.setter
    def ubicacion(self, value:str) -> None:
        if isinstance(value, str):
            self._ubicacion = value
        else:
            raise ValueError('Expected str')


