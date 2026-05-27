lista = []
continuacao = 'S'
while continuacao == 'S':
    print('-=-' * 10)
    valor = int(input("Digite um número: "))
    print('Valor adicionado com sucesso...')
    continuacao = str(input("Deseja continuar? [S/N]: ")).strip().upper()
    if continuacao == 'N':

    if not(valor in lista):
        lista.append(valor)

    if continuacao == 'N':
        print('-=-' * 10)
        lista.sort()
        print(f"Voce digitou os numeros {lista}")