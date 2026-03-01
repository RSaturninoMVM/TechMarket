class CarretCompra:
    def __init__(self):
        self.lista_productes = []

    def afegir(self, producte):
        self.lista_productes.append(producte)

    def checkout(self):
        tiquet = "\n--- TIQUET DE COMPRA ---\n"
        total = 0
        for p in self.lista_productes:
            tiquet += f"- {p.nom}: {p.preu}€\n"
            total += p.preu
        
        tiquet += "------------------------\n"
        tiquet += f"TOTAL A PAGAR: {total}€"
        return tiquet