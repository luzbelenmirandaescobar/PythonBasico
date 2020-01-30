class Vehiculo:
    DISTANCIA_BASE=12
    FACTOR_EMISION_GASOLINA=2.196
    FACTOR_EMISION_DIESEL=2.471
    def __init__ (self, placa, color, marca, modelo, combustible, km, tanque, AC): 
        self.placa=placa
        self.color=color
        self.marca=marca
        self.modelo=modelo
        self.combustible=combustible
        self.km=km
        self.tanque=tanque
        self.AC=AC
        self.encendido= False
        self.litros_consumidos=0


    # def encender(self): 
    #     if self.encendido == False: 
    #        self.encendido = True
    #     else: 
    #         print ("el familiar ya esta encendido")
         

    # def apagado(self):
    #         self.encendido= False

    def tocar_bocina(self):
        print("piii piii")

    def frenar(self):
        print("frenando...")

    def cargar_combustible(self, litros):
        self.tanque+=litros
        print("cargando combustible")

    def recorrer_distancia(self, distancia):
        if self.motor.esta_encendido():
            variante= self.obtener_variante()
            if distancia < (self.tanque*variante):
                self.km += distancia
                total_litros= round(self.km/variante)
                self.tanque -= total_litros
                self.litros_consumidos += total_litros
                print("recorriendo{}kilometros".format(distancia))
            else: 
                print("no tiene suficiente combustible")
        else:
            print("el vehiculo esta apagado")

                 

    
    def mostrar_vehiculo(self):
        print("La placa es: " + self.placa)
        print("El color es: " + self.color)
        print("La marca es: " + self.marca)
        print("el modelo es: " + self.modelo)
        print("el combustible es: " + self.combustible)
        print("el km es: " + str(self.km))
        print("el tanque es: " + str(self.tanque))
        print("el AC esta: " + str(self.AC))

    def calcular_CO2(self):
        if self.combustible=="gasolina":
           return (self.FACTOR_EMISION_GASOLINA*self.litros_consumidos)
        else:
            return (self.FACTOR_EMISION_DIESEL*self.litros_consumidos)

    def poner_motor(self, motor):
        self.motor= motor

    def obtener_variante(self):
        cilindrada = self.motor.obtenercilindrada()
        if cilindrada == 1000:
          return(12)
        elif cilindrada == 200:
            return(14)
        else:
            return(8)

    def hay_combustible(self, distancia):
        variante = self.obtener_variante()
        if not distancia < (variante*self.tanque):
            return False
        
        return True

    def obtener_informe(self):
        informe="\n-----------"
        informe+="\n INFORME_FINAL-EMISION CO2"
        informe+="\n----------"
        informe+="\n ud esta construyendo un vehiculo marca{}, modelo{}, color{}".format(self.marca, self.modelo, self.color)
        informe+="\n ha recorrido un total de{} km de distancia".format(self.km)
        informe+="\n ha consumido un total de{} litros de{}".format(self.litros_consumidos, self.combustible)
        informe+="\n en su tanque tiene{} litros de{}".format(self.tanque, self.combustible)
        informe+="\n se cambio a la atmosfera un total de {} km de CO2".format(round(self.calcular_CO2(),2))
    
        return informe

    

    


        




    