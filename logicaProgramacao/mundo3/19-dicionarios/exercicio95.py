jogadores= []
jogador= {}
contador= 0

continuar = ''
while 'N' not in continuar:
    nome = input("Nome do jogador: ")
    partidas = int(input(f"Quantas partidas {nome} jogou? "))
    gols = list()
    for i in range (0 ,partidas):
        gol = int(input(f"Quantos gols na partida {i}?"))
        gols.append(gol)
    jogador = {"cod": contador, "nome": nome, "gols" :gols, "total" :sum(gols)}
    contador += 1
    jogadores.append((jogador.copy()))
    continuar = input("Quer continuar? [S/N] ").upper()
    if continuar != 'S' and continuar != 'N':
        print("Erro! Digite apenas com S ou N")

print("-=" * 30)
for i in jogador.keys():
    print(f"{i:<15}", end="")
print("")
print("-" *60)
for k, v in enumerate(jogadores):
    for d in v.values():
        print(f"{str(d):<15}", end='')
    print()
print("-" * 60)

continuar_jogador = ''
while 'N'not in continuar_jogador:
    codigo = int(input("Mostrar dado de qual jogador? "))
    for i in jogadores:
        if codigo == i["cod"]:
            print(f"-- LEVANTAMENTO DO JOGADOR {i["nome"]}:")
            for c, v in enumerate(i["gols"]):
                print(f"No jogo {c + 1} fez {v} gols.")
        elif codigo >= len(jogadores) and codigo != 999:
            print(f"ERRO! Não existe jogador com código {codigo}. Tente novamente!")
        elif codigo == 999:
            print("<<< VOLTE SEMPRE >>>")
            continuar_jogador = False