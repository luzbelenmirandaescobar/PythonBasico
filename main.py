from motor import Motor
from vehiculo import Vehiculo 
from simulador import Simulador

L = Motor("45756", 1000)
U = Motor("33687", 1000)

familiar = Vehiculo("46578GYH","azul","nissan","2015","gas",1000,40.1, True) 
rapido = Vehiculo("374654STB","rojo","toyosa","2010","gas",1000,40.4,True)

familiar.poner_motor(L)
rapido.poner_motor(U)

lista=[familiar,rapido]
S = Simulador(lista)
S.iniciar_simulacion(2)