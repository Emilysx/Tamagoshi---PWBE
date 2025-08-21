from tamagoshi import Tamagoshi

class Fadas(Tamagoshi):
    def __init__(self, nome, pozinho = 50, energia_voar = 50):
        super().__init__(nome)
        self.pozinho = pozinho # PEDIR AJUDA PARA MARY
        self.energia_voar = energia_voar

    def recarregar_pozinho_magico(self):  
        if self.pozinho < 100:
            print(f"{self.nome} espalhou brilho mágico e recarregou seu pozinho encantado!")
            self.pozinho = min(100, self.pozinho + 20)
        else:
            print("O pozinho mágico de {self.nome} já está transbordando de magia!")

    def voar(self):
        if self.pozinho >= 10:
            print(f"{self.nome} bateu suas asas delicadas e saiu voando pelo céu estrelado!")
            self.pozinho = max(0, self.pozinho - 10)
            self.tedio = min(100, self.tedio - 20)
            self.saude = min(100, self.saude + 20)
        else: 
            print (f"{self.nome} tentou voar, mas seu pozinho mágico está fraco demais...")

    def fazer_travessuras(self):
        if self.pozinho >=10:
            print(f"{self.nome} pregou uma travessura brilhante e divertida, espalhando risadinhas pela floresta!")
            self.pozinho = max(0, self.pozinho - 10)
            self.energia_voar = max(0, self.energia_voar - 15)
            self.tedio = max(0, self.tedio - 25)
        else:
            print(f"{self.nome} queria aprontar, mas sem pozinho mágico as travessuras não funcionam...")

    def banho_de_lunar(self):
        print(f"{self.nome} dançou sob a luz da lua e tomou um banho de luar prateado... agora está revigorada!!")
        self.energia_voar = min(100, self.energia_voar + 50)
        self.saude = min(100, self.saude + 20)
        self.fome = min(100, self.fome + 15)

#########################################################################################################################################

class Sereias(Tamagoshi):
    class Sereias(Tamagoshi):
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

    def cantar_para_os_peixes(self):
        if self.canto_magico >= 10:
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



