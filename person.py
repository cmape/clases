class Persona(object):
    def __init__(self,nombre,edad,genero,estatura):
        self.nombre = nombre
        self.edad = edad
        self.genero= genero
        self.estatura = estatura
        
    def presentarse (self):
        print("Hola, mi nombre es {}  y tengo {} años de edad". format(self.nombre,self.edad))     
        

    def caminar (self):
        print("el avatar esta en movimiento")
       
print("////////////////informacion del primer objeto//////////////")
print("")
persona1=Persona("camilo",22,"masculino",170)

persona1.presentarse()
persona1.caminar()

class Afro(Persona):
    def __init__ (self,nombre,edad,genero,estatura,cabello):
        super().__init__(nombre,edad,genero,estatura)
        self.cabello=cabello
        
    def cantar (self):
        print("estoy cantando y me fascina")
        
print("")
print("////////////////informacion del segundo objeto//////////////")
print("")
afro=Afro("mateo", 30, "masculino", 167,"rizado")      
afro.presentarse()
print("como soy afro mi cabello es ",afro.cabello)
afro.caminar()
afro.cantar()
    
        
class Asiatico(Persona):
    def __init__ (self,nombre,edad,genero,estatura,cabello,ojos):
        super().__init__(nombre,edad,genero,estatura)
        self.ojos=ojos
        
    def luchar (self):
        print("Soy experto en artes mixtas ")
                
print("")
print("////////////////informacion del tercer objeto//////////////")
print("")
asiatico=Asiatico("yakima", 32, "femenino", 150,"lasio","razgados")      
asiatico.presentarse()
print("como soy asiatico mis ojos son ",asiatico.ojos)
asiatico.caminar()
asiatico.luchar()
