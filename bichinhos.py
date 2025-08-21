from tamagoshi import Tamagoshi

class Fadas(Tamagoshi):
    def __init__(self, nome, pozinho, voar):
        super().__init__(nome)
        self.pozinho = 50
        self.voar = 100

    def regarca_pozinho_magico(self): #arrumar 
        if self.pozinho < 100:
            print(f"{self.nome} regarregou pozinho mágico")
            self.saude = min(100, self.saude + 20)
            self.pozinho = max(0, self.pozinho - 10)
        else:
            print("Pozinho insufifiente para usar.")

    def voar(self):
        if self.pozinho >= 10:
            print(f"{self.nome} saiu para voar!")
            self.pozinho = max(0, self.pozinho - 10)
            self.tedio = min(100, self.tedio + 20)
            self.saude = min(100, self.saude + 15)


