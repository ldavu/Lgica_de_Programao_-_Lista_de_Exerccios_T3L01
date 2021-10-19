import random

vida_jogador = 100
vida_boss = 100

tirar_vida = random.randint(14,25)
tirar_vida_boss = random.randint(12,15)

print("digite 'bater' para matar o boss")
resposta_bater = str(input)

while (vida_jogador > 0):

    resposta_bater = str(input())
    
    if (resposta_bater == "bater"):
        print("/n"*25)
        vida_boss = vida_boss - tirar_vida
        vida_jogador = vida_jogador - tirar_vida_boss
        print(f"Você tirou {tirar_vida}")
        print(f"Vida do boss {vida_boss}")
        print(f"Sua vida {vida_jogador}")

    if (vida_jogador <= 0):
        print("Você morreu...")

    if (vida_boss <= 0):
        print("Parabéns jogador você matou o boss!")
        
