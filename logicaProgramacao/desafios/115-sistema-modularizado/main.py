from rich import print
from rich.table import Table
pessoas = {
    'sei la': 12,
    'fds': 15
}
def mostrarMenu():
    print("-="*15)
    print("      MENU PRINCIPAL")
    print("-="*15)
    print("[bold blue]1 - Ver pessoas cadastradas\n2 - Cadastrar nova pessoa\n3 - Sair do sistema")
def mostrarPessoas():
    print("-="*15)
    print("      PESSOAS CADASTRADAS")
    print("-="*15)
    tabela = Table()
    tabela.add_column('nome')
    tabela.add_column('idade')
    for pessoa in pessoas:
        tabela.add_row(f"{pessoa}", f"{pessoas[pessoa]}")
        tabela.add_row(f"──────", "──────")

    print(tabela)
def cadastrarPessoas():
    print("-="*15)
    print("      NOVO CADASTRADO")
    print("-="*15)
    nome = input("Nome: ")
    pessoas[nome] = int(input("Idade: "))
opcao = 0
while opcao != 3:
    mostrarPessoas()
    print("[bold yellow]Sua opção: [/]", end='')
    opcao = int(input())
    if opcao == 1:
        mostrarPessoas()
    elif opcao == 2:
        cadastrarPessoas()