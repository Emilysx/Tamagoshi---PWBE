import sys
from time import sleep

RESET = "\033[0m"
COLORS = [
    "\033[35m",
    "\033[35m",
    "\033[35m",
]

def printLyrics():
    lines = [
        ("TES-", 0.06),
        ("TEST-", 0.05),
        ("TESTESSS-", 0.04),
    ]

    for i, (line, delay) in enumerate(lines):
        color = COLORS[i % len(COLORS)]  # Escolhe a cor
        for char in line:
            sys.stdout.write(f"{color}{char}{RESET}")
            sys.stdout.flush()  # Força a saída imediata
            sleep(delay)  # Espera antes de escrever o próximo caractere
        sys.stdout.write("\n")  # Quebra de linha após cada linha
        sleep(0.3)  # Pequena pausa antes da próxima linha

printLyrics()
