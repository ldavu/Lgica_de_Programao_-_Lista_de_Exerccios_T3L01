sair_programa = 'sim'

entregas = 0
retirar = 0

while (sair_programa != "sim"):
    print("Olá entregador! Você o que você vai fazer? entregar | retirar | sair")
    resposta = str(input())

    if(resposta == "entregar"):
        retirar += 1
    elif(resposta == "entregar"):
        entregas += 1

    print("Deseja sair do programa?")
    resposta_sair = str(input())
    if(resposta_sair == "sim"):
        print("você saiu do programa!")
