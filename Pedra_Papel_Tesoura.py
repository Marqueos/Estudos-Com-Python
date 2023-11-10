import secrets

def Pedra_papel_tesoura():
    Escolhas = ['Pedra', 'Papel', 'Tesoura']

    Jogada_computador1 = secrets.SystemRandom().choice(Escolhas)
    Jogada_computador2 = secrets.SystemRandom().choice(Escolhas)
    
    print("Jogada do computador1:", Jogada_computador1)
    print("Jogada do computador2:", Jogada_computador2)

    return determinar_vencedor(Jogada_computador1, Jogada_computador2)

def determinar_vencedor(jogada1, jogada2):
    if jogada1 == jogada2:
        return "Empate"
    elif (
        (jogada1 == "Pedra" and jogada2 == "Tesoura") or
        (jogada1 == "Papel" and jogada2 == "Pedra") or
        (jogada1 == "Tesoura" and jogada2 == "Papel")
    ):
        return "Computador1 vence"
    else:
        return "Computador2 vence"

def Principal():
    total_jogadas = 10000
    vitorias_computador1 = 0
    vitorias_computador2 = 0
    empates = 0 
    
    for _ in range(total_jogadas):
        resultado = Pedra_papel_tesoura()
        print(resultado)

        if resultado == "Computador1 vence":
            vitorias_computador1 += 1
        elif resultado == "Computador2 vence":
            vitorias_computador2 += 1
        elif resultado == "Empate":
            empates += 1
    print("\nResultado final:")
    print(f"Computador1 venceu {vitorias_computador1} vezes.")
    print(f"Computador2 venceu {vitorias_computador2} vezes.")
    print(f"Quantidade de empates foi de: {empates} vezes.")
    

    if vitorias_computador1 > vitorias_computador2:
        print("Computador1 é o grande vencedor!")
    elif vitorias_computador2 > vitorias_computador1:
        print("Computador2 é o grande vencedor!")
    else:
        print("Houve um empate geral!")

# Chamar a função Principal
Principal()
