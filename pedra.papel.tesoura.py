print("---> PEDRA, PAPEL, TESOURA <---")
jogador1 = input("Digite o nome do primeiro jogador: ")
jogador2 = input("Digite o nome do segundo jogador: ")
empate = 0
vitoria1 = 0
vitoria2 = 0
for x in range(3):
    print()
    jgd1 = input(f"{jogador1} Escolha pedra, papel ou tesoura: ").lower()
    while jgd1 not in ["pedra", "papel", "tesoura"]:
        jgd1 = input("Opção inválida. Escolha Pedra, Papel ou Tesoura: ").lower()
    jgd2 = input(f"{jogador2} Escolha pedra, papel ou tesoura: ").lower()
    while jgd2 not in ["pedra", "papel", "tesoura"]:
        jgd2 = input("Opção inválida. Escolha pedra, papel ou tesoura: ").lower()
    print(f"{jogador1} escolheu: {jgd1}")
    print(f"{jogador2} escolheu: {jgd2}")
    if jgd1 == jgd2:
        print("O jogo foi empate")
        empate += 1
    if jgd1 == "pedra" and jgd2 == "papel" or jgd1 == "papel" and jgd2 == "tesoura" or jgd1 == "tesoura" and jgd2 == "pedra":
        print(f"{jogador2} GANHOOOU!!! ")
        vitoria2 += 1
    elif jgd2 == "pedra" and jgd1 == "papel" or jgd2 == "papel" and jgd1 == "tesoura" or jgd2 == "tesoura" and jgd1 == "pedra":
        print(f"{jogador1} GANHOOOU!!! ")
        vitoria1 += 1
print()
print(f"O jogo terminou empatado {empate}x")
print(f"{jogador1} ganhou {vitoria1}x e {jogador2} ganhou {vitoria2}x")
if vitoria1 > vitoria2:
    print(f"{jogador1} foi o campeão com {vitoria1} vitórias")
elif vitoria2 > vitoria1:
    print(f"{jogador2} foi o campeão com {vitoria2} vitórias")
else:
    print("O resultado final foi empate")
