import random
from time import sleep

vida_jogador = 100



while (vida_jogador > 0):
    
    ataque = random.randint(15,24)

    vida_jogador = vida_jogador - ataque
    sleep(1)

    print(f"o inimigo tirou {ataque}")
    print(f"Sua vida {vida_jogador}")

    if (vida_jogador <= 0):
        print("Você perdeu...")

