sair_programa = ""

entregas = 0
retirar = 0

while (sair_programa != "não"):
    print("Olá entregador! Você o que você vai fazer? entregar | retirar | sair")
    resposta = input()

    if(resposta == "retirar"):
        retirar += 1
    elif(resposta == "entregar"):
        entregas += 1

    print("Deseja sair do programa?")
    resposta_sair = str(input())
    if(resposta_sair == "sim"):
        print("você saiu do programa!")
        print("-"*15)
        if(entregas > 1):print(f"Você fez {entregas} entregas")
        else:print(f"Você fez {entregas} entrega")
        print(f"Você retirou {retirar}")
