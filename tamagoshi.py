class Tamagoshi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0        
        self.saude = 100    
        self.idade = 0       
        self.tedio = 0       
        self.avisos_fome = 0 
        self.avisos_tedio = 0 

    # Alimentar diminui a fome
    def alimentar(self):
        print(f"{self.nome} se alimentou certinhoo")
        self.fome -= 10

    def brincar(self):
            print(f"{self.nome} brincou por horas")
            self.tedio -= 5

    # def sair(self):
    #     print(f"\n👋 {self.nome} se despede por agora... até a próxima!")
    #     return True

    # Atualiza saúde de acordo com fome e tédio
    def vida(self):
        # Redução de saúde progressiva
        if (50 < self.fome <= 60) or (50 < self.tedio <= 60):
            self.saude -= 10
        elif (60 < self.fome <= 80) or (60 < self.tedio <= 80):
            self.saude -= 30
        elif (80 < self.fome <= 90) or (80 < self.tedio <= 90):
            self.saude -= 50

        # Avisos de perigo
        if self.fome >= 100:
            if self.avisos_fome < 3:
                print(f"⚠️ {self.nome} está com fome extrema! Precisa comer agora!")
                self.avisos_fome += 1
            self.fome = 100

        if self.tedio >= 100:
            if self.avisos_tedio < 3:
                print(f"⚠️ {self.nome} está muito entediado(a)! Precisa brincar!")
                self.avisos_tedio += 1
            self.tedio = 100

        # Garante que a saúde nunca fique negativa
        self.saude = max(0, int(self.saude))

    # Tempo passando: idade aumenta, fome e tédio aumentam
    def tempoPassando(self):
        self.idade += 0.2
        self.tedio = min(100, int(self.tedio + 2))  # exemplo: tédio sobe devagar
        self.fome = min(100, int(self.fome + 5))    # exemplo: fome sobe mais rápido
        self.vida()  # atualiza saúde e mostra avisos


