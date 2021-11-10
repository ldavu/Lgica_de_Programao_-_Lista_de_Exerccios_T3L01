vida_jogador = 100
vida_boss = 100

while (vida_jogador > 0) and (vida_boss > 0):
    tirar_vida = int(input("adiciona texto"))
    tirar_vida_boss = int(input("adciona texto"))
    vida_boss = vida_boss - tirar_vida
    vida_jogador = vida_jogador - tirar_vida_boss
    print(f"Vida do boss: {vida_boss} pontos")
    print(f"Sua vida: {vida_jogador} pontos")
if (vida_jogador <= 0):
    print("Você morreu...")
if (vida_boss <= 0):
    print("Parabéns jogador você matou o boss!")
