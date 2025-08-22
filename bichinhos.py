from tamagoshi import Tamagoshi
from teste import musica_filme

class Fada(Tamagoshi):
    def __init__(self, nome, pozinho = 50, energia_voar = 50):
        super().__init__(nome)
        self.pozinho = pozinho # PEDIR AJUDA PARA MARY
        self.energia_voar = energia_voar

    def recarregar_pozinho_magico(self):  
        if self.pozinho < 100:
            print(f"{self.nome} espalhou brilho mágico e recarregou seu pozinho encantado!")
            self.pozinho += 30
        else:
            print(f"O pozinho mágico de {self.nome} já está transbordando de magia!")

    def voar(self):
        if self.pozinho >= 10:
            print(f"{self.nome} bateu suas asas delicadas e saiu voando pelo céu estrelado!")
            self.pozinho -= 10
            self.tedio -= 20
            self.saude += 5
        else: 
            print (f"{self.nome} tentou voar, mas seu pozinho mágico está fraco demais...")

    def fazer_travessuras(self):
        if self.pozinho >=10:
            print(f"{self.nome} pregou uma travessura brilhante e divertida, espalhando risadinhas pela floresta!")
            self.pozinho -= 20
            self.energia_voar -= 25
            self.tedio -= 25
        else:
            print(f"{self.nome} queria aprontar, mas sem pozinho mágico as travessuras não funcionam...")

    def banho_de_lunar(self):
        print(f"{self.nome} dançou sob a luz da lua e tomou um banho de luar prateado... agora está revigorada!!")
        #if self.energia_voar <= 100:

        self.energia_voar += 50
        self.saude += 20
        self.fome += 15

#########################################################################################################################################

class Sereia(Tamagoshi):
    def __init__(self, nome, energia_nadando=50, canto_magico=50, alegria=50):
        super().__init__(nome)
        self.energia_nadando = energia_nadando  
        self.canto_magico = canto_magico        
        self.alegria = alegria                  

    def nadar_nas_correntes(self):
        if self.energia_nadando >= 10:
            print(f"{self.nome} deslizou pelas correntes do oceano, brincando entre as ondas cintilantes!")
            self.energia_nadando = max(0, self.energia_nadando - 15)
            self.tedio = max(0, self.tedio - 20)
            self.saude = min(100, self.saude + 10)
            self.alegria = min(100, self.alegria + 15)
        else:
            print(f"{self.nome} está cansada e precisa descansar antes de nadar novamente... ")

    def canto_sereia(self):
        if self.canto_magico >= 10:
            musica_filme()
            print(f"{self.nome} cantou uma melodia encantada e todos os peixinhos dançaram ao seu redor!")
            self.canto_magico = max(0, self.canto_magico - 15)
            self.tedio = max(0, self.tedio - 25)
            self.alegria = min(100, self.alegria + 20)
        else:
            print(f"{self.nome} está sem energia suficiente para cantar seu lindo canto...")

    def encontrar_perolas_magicas(self):
        print(f"{self.nome} encontrou pérolas mágicas brilhando no fundo do mar e guardou como tesouro!")
        self.tedio = max(0, self.tedio - 15)
        self.saude = min(100, self.saude + 10)
        self.alegria = min(100, self.alegria + 15)

    def brincar_com_delfins(self):
        if self.energia_nadando >= 10:
            print(f"{self.nome} nadou junto com golfinhos brincalhões, rindo e pulando entre as ondas!")
            self.energia_nadando = max(0, self.energia_nadando - 10)
            self.tedio = max(0, self.tedio - 30)
            self.alegria = min(100, self.alegria + 20)
        else:
            print(f"{self.nome} está muito cansada para brincar com os golfinhos...")

    def descansar_na_ondinha(self):
        print(f"{self.nome} deitou sobre uma onda suave e deixou a brisa do mar renovar suas forças...")
        self.energia_nadando = min(100, self.energia_nadando + 30)
        self.saude = min(100, self.saude + 20)
        self.tedio = min(100, self.tedio + 5)
        self.alegria = min(100, self.alegria + 10)


#########################################################################################################################################  

class PrincesaArcoIris(Tamagoshi):
    def __init__(self, nome, energia_magica=50):
        super().__init__(nome)  
        self.energia_magica = energia_magica  

    def criar_arco_iris(self):
        if self.energia_magica >= 10:
            print(f"{self.nome} levantou as mãos e criou um arco-íris radiante que iluminou tudo!")
            self.energia_magica = max(0, self.energia_magica - 15)
            self.tedio = max(0, self.tedio - 20)
            self.fome = max(0, self.fome - 10)
            self.saude = min(100, self.saude + 15)
        else:
            print(f"{self.nome} está sem energia mágica suficiente para criar o arco-íris...")

    def dançar_nas_cores(self):
        if self.energia_magica >= 5:
            print(f"{self.nome} dançou entre as cores do arco-íris, espalhando magia pelo ar! ")
            self.energia_magica = max(0, self.energia_magica - 10)
            self.tedio = max(0, self.tedio - 25)
            self.fome = max(0, self.fome - 5)
            self.saude = min(100, self.saude + 10)
        else:
            print(f"{self.nome} está cansada e precisa recuperar energia mágica antes de dançar.")

    def espalhar_po_magico(self):
        if self.energia_magica >= 10:
            print(f"{self.nome} espalhou pó mágico colorido, deixando tudo mais brilhante e cheio de vida! ")
            self.energia_magica = max(0, self.energia_magica - 15)
            self.tedio = max(0, self.tedio - 20)
            self.saude = min(100, self.saude + 15)
        else:
            print(f"{self.nome} não tem energia mágica suficiente para espalhar pó colorido...")

    def descansar_no_arco_iris(self):
        print(f"{self.nome} se deitou sobre um arco-íris suave e deixou sua saúde se renovar...")
        self.energia_magica = min(100, self.energia_magica + 50)
        self.saude = min(100, self.saude + 25)
        self.tedio = min(100, self.tedio + 5)
        self.fome = max(0, self.fome - 15)