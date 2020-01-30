import random
class Simulador:
    
    def __init__(self, vehiculos):
        self.vehiculos=vehiculos

    def iniciar_simulacion(self, dias):
        for a in self.vehiculos:
            print("\n")
            print("VEHICULO{}".format(a.placa))
            if not a.motor.esta_encendido():
               a.motor.encender()
            for dia in range (1,dias+1):
                print("----------")
                print("Dia # {}".format(dia))
                print("----------")
                distancia=random.randint(0,100)
                if not a.hay_combustible(distancia):
                    litros=random.randint(30,60)
                    a.cargar_combustible(litros)
                a.recorrer_distancia(distancia)
            print(a.obtener_informe())