#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
#No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média

dicionario = {}
lista = []
media = 0
mulheres = []
acima_idade = []
opc = ''
while 'N' not in opc:
    dicionario['NOME'] = input("Digite seu nome: ").upper().strip()
    dicionario['SEXO'] = input("Digite seu sexo[M/F]: ").upper()
    if dicionario['SEXO'] != 'M' and dicionario['SEXO'] != 'F':
        print("Coloque o sexo corretamente!!")
    if dicionario['SEXO'] == 'F':
        mulheres.append(dicionario['NOME'])
    dicionario['IDADE'] = int(input("Digite a sua idade: "))
    if dicionario['IDADE'] >18:
        acima_idade.append(dicionario['NOME'])
    media += dicionario['IDADE']
    lista.append(dicionario.copy())
    opc = input("Deseja continuar?[S/N] ").upper()
print(f"A quantidade de pessoas cadastradas {len(lista)}")
print(f"A media de idade de todas as pessoas cadastradas é {media / len(lista):.2f}")
print(f"A lista de todas as mulheres cadastradas é {mulheres}")
print(f"Os maiores de idade sao {acima_idade}")
