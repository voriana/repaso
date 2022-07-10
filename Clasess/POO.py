class Casa:
    #metod constructor, con un parametro de entrada(color)
    def __init__(self, color):
        self.color=color
        self.consumo_de_luz=0
        self.consumo_de_agua=0

    #funciones/metodos de la clase Casa
    def pintar(self,color):
        self.color=color
    
    def prender_luz(self):
        self.consumo_de_luz+=10
    
    def abrir_ducha(self):
        self.consumo_de_agua+=12

    def tocar_timbre(self):
        print("RINGGG")
        self.consumo_de_luz+=5

# Creación de objeto o instancia de clase
miCasa=Casa("blanca")
print("El color de mi casa es "+ miCasa.color)

miCasa.prender_luz()
print(miCasa.consumo_de_luz)


#HERENCIA
class Mansion(Casa):
    def prender_luz(self):
        self.consumo_de_luz+=50
    
    def abrir_ducha(self):
        self.consumo_de_agua+=50
    
    def tocar_timbre(self):
        print("DING-DONG")
        self.consumo_de_luz+=9

miMansion=Mansion("Blanca")
miMansion.pintar("Verde")

print(miMansion.color)
print(miMansion.consumo_de_luz)