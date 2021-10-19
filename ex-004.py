pontos = 100
pontos_jogador = 0
arremessos = 0
metro5 = 20 #>
metro2 = 10 #>
metro = 5   #<=


while(pontos_jogador < 100):
    print('Qual metro você lançou até a cesta?')
    resposta = int(input())

    if(resposta > 5):
        pontos_jogador = pontos_jogador + metro5
        arremessos += 1
    elif(resposta > 2):
        pontos_jogador = pontos_jogador + metro2
        arremessos += 1
    elif(resposta <= 2):
        pontos_jogador = pontos_jogador + metro
        arremessos += 1
    
    if(pontos_jogador >= pontos):
        print(f"Você atingiu {pontos_jogador} pontos!")
