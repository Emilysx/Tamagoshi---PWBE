from tamagoshi import Tamagoshi
from bichinhos import Fada, Sereia, PrincesaArcoIris
from time import sleep

def main():
    aviso_fome = 0
    aviso_tedio = 0

    print("✨ Bem-vindo ao Mundo dos Tamagoshis Encantados ✨")
    print("Escolha seu companheiro(a) mágico:")
    print("1 - Fada 🧚")
    print("2 - Sereia 🧜‍♀️")
    print("3 - Princesa do Arco-Íris 🌈")

    escolha = input("Digite o número da sua escolha: ")
    nome = input("Dê um nome para seu novo companheiro(a): ")

    if escolha == "1":
        criatura = Fada(nome)
    elif escolha == "2":
        criatura = Sereia(nome)
    elif escolha == "3":
        criatura = PrincesaArcoIris(nome)
    else:
        print("Opção inválida! Criando uma Fada por padrão...")
        criatura = Fada(nome)

    print(f"\n✨ {criatura.nome} nasceu no mundo encantado! Cuide bem dela! ✨\n")

    while True:
        # >>> Atualiza estado com o tempo passando
        criatura.tempoPassando()

        # Converte valores para inteiros
        criatura.fome = int(criatura.fome)
        criatura.tedio = int(criatura.tedio)
        criatura.idade = int(criatura.idade)

        # Mensagens de alerta
        if criatura.fome >= 100 and aviso_fome < 3:
            print(f"⚠️ {criatura.nome} está com muita fome! Dê comida! ")
            aviso_fome += 1
        if criatura.tedio >= 100 and aviso_tedio < 3:
            print(f"⚠️ {criatura.nome} está muito entediado(a)! Brinque com ele(a)!")
            aviso_tedio += 1

        # Verifica se o bichinho morreu
        if criatura.saude <= 0 or criatura.fome >= 100 or criatura.tedio >= 100:
            print(f"\n💀 {criatura.nome} morreu... Fim de jogo.")
            break

        # STATUS da criatura
        if isinstance(criatura, Fada):
            print(f"\n\033[1;36mSTATUS (Fada)\033[0m | "
                  f"\033[33mNome:\033[0m {criatura.nome} | "
                  f"\033[32mSaúde:\033[0m {criatura.saude} | "
                  f"\033[31mFome:\033[0m {criatura.fome} | "
                  f"\033[35mTédio:\033[0m {criatura.tedio} | "
                  f"\033[34mPozinho:\033[0m {criatura.pozinho} | "
                  f"\033[95mEnergia Voar:\033[0m {criatura.energia_voar} | "
                  f"\033[36mIdade:\033[0m {criatura.idade}"
            )
            print("0 - Sair do jogo")
            print("1 - Recarregar pozinho mágico")
            print("2 - Voar")
            print("3 - Fazer travessuras")
            print("4 - Tomar banho de luar")
            print("5 - Alimentar")
            print("6 - Brincar")

        elif isinstance(criatura, Sereia):
            print(f"\n\033[1;36mSTATUS (Sereia)\033[0m | "
                  f"\033[33mNome:\033[0m {criatura.nome} | "
                  f"\033[32mSaúde:\033[0m {criatura.saude} | "
                  f"\033[31mFome:\033[0m {criatura.fome} | "
                  f"\033[35mTédio:\033[0m {criatura.tedio} | "
                  f"\033[95mEnergia Nadar:\033[0m {criatura.energia_nadando} | "
                  f"\033[96mCanto:\033[0m {criatura.canto_magico} | "
                  f"\033[92mAlegria:\033[0m {criatura.alegria} | "
                  f"\033[36mIdade:\033[0m {criatura.idade}"
            )       
            print("0 - Sair do jogo")
            print("1 - Nadar nas correntes")
            print("2 - Cantar para os peixes")
            print("3 - Encontrar pérolas mágicas")
            print("4 - Brincar com os golfinhos")
            print("5 - Descansar na ondinha")
            print("6 - Alimentar")
            print("7 - Brincar")

        elif isinstance(criatura, PrincesaArcoIris):
            print(f"\n\033[1;36mSTATUS (Princesa Arco-Íris)\033[0m | "
                  f"\033[33mNome:\033[0m {criatura.nome} | "
                  f"\033[32mSaúde:\033[0m {criatura.saude} | "
                  f"\033[31mFome:\033[0m {criatura.fome} | "
                  f"\033[35mTédio:\033[0m {criatura.tedio} | "
                  f"\033[95mEnergia Mágica:\033[0m {criatura.energia_magica} | "
                  f"\033[36mIdade:\033[0m {criatura.idade}"
            )
            print("0 - Sair do jogo")
            print("1 - Criar arco-íris")
            print("2 - Dançar nas cores")
            print("3 - Espalhar pó mágico")
            print("4 - Descansar no arco-íris")
            print("5 - Alimentar")
            print("6 - Brincar")


        acao = input("Escolha: ")

        if acao == "0":
            print(f"\n👋 {criatura.nome} se despede por agora... até a próxima!")
            break

        # Ações específicas
        elif isinstance(criatura, Fada):
            if acao == "1": criatura.recarregar_pozinho_magico()
            elif acao == "2": criatura.voar()
            elif acao == "3": criatura.fazer_travessuras()
            elif acao == "4": criatura.banho_de_lunar()
            elif acao == "5": criatura.alimentar()
            elif acao == "6": criatura.brincar()


        elif isinstance(criatura, Sereia):
            if acao == "1": criatura.nadar_nas_correntes()
            elif acao == "2": criatura.canto_sereia()
            elif acao == "3": criatura.encontrar_perolas_magicas()
            elif acao == "4": criatura.brincar_com_delfins()
            elif acao == "5": criatura.descansar_na_ondinha()

        elif isinstance(criatura, PrincesaArcoIris):
            if acao == "1": criatura.criar_arco_iris()
            elif acao == "2": criatura.dançar_nas_cores()
            elif acao == "3": criatura.espalhar_po_magico()
            elif acao == "4": criatura.descansar_no_arco_iris()

        sleep(1.5)


if __name__ == "__main__":
    main()
