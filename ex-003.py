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
    resposta_sair = str(input("Deseja sair do programa?"))
    if(resposta_sair == "sim"):
        print("você saiu do programa!")
        print(f"Você entregou: {entregas}\nVocê retirou: {retirar}
