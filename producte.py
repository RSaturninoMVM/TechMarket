class Producte:
    def __init__(self, nom, preu, stock):
        self.nom = nom
        self.__preu = preu  
        self.stock = stock

    def get_preu_web(self):
        return self.__preu * 1.21

    def vendre(self, quantitat):
        if quantitat <= self.stock:
            missatge = f'✅ Venda realitzada: {quantitat} de {self.stock}'
            self.stock -= quantitat
            return missatge
        return f'❌ Error: No hi ha prou stock de {self.nom}'

    @property
    def preu(self):
        return self.__preu