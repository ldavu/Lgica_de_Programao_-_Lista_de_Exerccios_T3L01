pontos = 100
pontos_jogador = 0
arremessos = 0

while(pontos_jogador < 100):
    resposta = int(input('Quantos metros você lançou até a cesta? '))

    if(resposta > 5):
        pontos_jogador += 20
        arremessos += 1
    elif(resposta > 2):
        pontos_jogador += 10
        arremessos += 1
    elif(resposta <= 2):
        pontos_jogador += 5
        arremessos += 1
    
    if(pontos_jogador >= pontos):
        print(f"Você atingiu {pontos_jogador} pontos em {arremessos} arremessos!")
