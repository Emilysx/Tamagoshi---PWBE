import sys
from time import sleep

RESET = "\033[0m"
COLORS = ["\033[35m"] * 20  # tudo lilás (ou pode variar se quiser)

def printLyrics():
    lines = [
        ("Chamando a sereias, a chance é agora", 0.08),   
        ("De saudar a Eris com a dança da hora", 0.08),  
        ("Ela arrasa, alucina, domina o mar", 0.08), 
        ("Altas ondas, majestade", 0.05),
        ("Também vamos pegar", 0.02),
        ("Sobre a onda deslizar", 0.07),
        ("Laidwer, Hanten vai se amarrar", 0.12),
        ("Pega essa onda pra no tubo entrar", 0.10),

        ("Fazendo Mahi-Mahi", 0.04),
        ("Vamos logo agitaaaarrrrrrrr", 0.05),
        ("É Rainha das Onda-a-a-s!", 0.09),
        ("Olha que maneiro ela sabe surfar", 0.06),
        ("É Rainha das Onda-a-a-s!", 0.09),
        ("E sua coroa", 0.07),
        ("Ninguém ousa tirar!", 0.07),
    ]

    for i, (line, delay) in enumerate(lines):
        color = COLORS[i % len(COLORS)]
        for char in line:
            sys.stdout.write(f"{color}{char}{RESET}")
            sys.stdout.flush()
            sleep(delay)
        sys.stdout.write("\n")
        sleep(0.4)  # pausa entre frases

printLyrics()