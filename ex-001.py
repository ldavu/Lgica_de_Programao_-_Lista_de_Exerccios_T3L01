vida_jogador = 100

while (vida_jogador > 0):
    
  ataque = int(input("adc texto aqui"))

  vida_jogador = vida_jogador - ataque

  print(f"O inimigo tirou: {ataque} pontos\nSua vida: {vida_jogador} pontos")
if (vida_jogador <= 0):
  print("Você perdeu...")
