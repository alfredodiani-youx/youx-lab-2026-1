def leiaDinheiro(preco):
    valido = False
    while not valido:
        valor = str(input(preco))
        if valor.isalpha() or valor.strip() == '':
            print('ERRO! Preço inválido!')
        else:
            valido = True
            return float(valor)


#Exercício 115
def mostrarMenu():
    print('-='*20)
    print('            MENU PRINCIPAL')
    print('-=' * 20)
    print('1 - Ver pessoas cadastradas\n2 - Cadastrar nova Pessoa\n3 - Sair do Sistema')
    print('-=' * 20)
pessoas = {
    'luiz': 15,
    'vini': 17
}
def mostrarPessoas():
    print('-='*20)
    print('           PESSOAS CADASTRADAS')
    print('-=' * 20)
    for nome in pessoas:
        print(nome, end=' ')
        print(pessoas[nome])

def cadastrarPessoas():
    print('-='*20)
    print('            NOVO CADASTRO')
    print('-=' * 20)
    pessoas[nome]
opcao = 0
while opcao != 3:
    mostrarMenu()
    opcao = int(input('Sua opção: '))

mostrarPessoas()