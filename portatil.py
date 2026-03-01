from producte import Producte

class Portatil(Producte):
    def __init__(self, nom, preu, stock, ram, processador):
        super().__init__(nom, preu, stock)
        self.ram = ram
        self.processador = processador

    def __str__(self):
        return f"PORTÀTIL: {self.nom} | {self.ram}GB RAM | {self.processador}"