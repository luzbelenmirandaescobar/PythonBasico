class Calculadora:
    def __init__ (self, numero1, numero2):
        self.numero1=numero1
        self.numero2=numero2

    def suma (self):
        try:
            r = self.numero1 + self.numero2
            print ("la suma de {} y {} es: {}".format(self.numero1, self.numero2, r))
        except TypeError:
            print("tipo de dato no debe ser numerico")
        except:
            print("error al sumar")

    def resta (self):
        try:
            r = self.numero1 - self.numero2
            print("la resta de {} y {} es: {}".format(self.numero1, self.numero2, r))
        except TypeError:
            print("tipo de dato no debe ser numerico")
        except:
            print("error al restar")

    def multiplicacion (self):
        try:
            r = self.numero1 * self.numero2
            print("la multiplicacion de {} y {} es: {}".format(self.numero1, numero2, r))
        except TypeError:
            print("tipo de dato no debe ser numerico")
        except:
            print("error al multiplicar")

    def division (self):
        try:
            r = self.numero1  / self.numero2 
            print("la division de {} y {} es: {}".format(self.numero1, self.numero2, r))
        except ZeroDivisionError:
            print("no se puede dividir entre cero") 
        except TypeError:
            print("tipo de dato no debe ser numerico") 
        except:
            print("error al divir")

    def pontencia (self):
        try:
            r = self.numero1 ** self.numero2
            print("la pontencia de {} y {} es: {}".fomart(self.numero1,self.numero2, r))
        except TypeError:
            print("tipo de dato no debe ser numerico")
        except:
            print("error al potenciar")
      

   

