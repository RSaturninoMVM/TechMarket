from producte import Producte

class Smartphone(Producte):
    def __init__(self, nom, preu, stock, camera):
        super().__init__(nom, preu, stock)
        self.camera = camera

    def get_preu_web(self):
        return (self.preu * 1.21) + 5