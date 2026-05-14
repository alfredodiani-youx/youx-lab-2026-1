from rich import print
from rich.panel import Panel

funcionarios = [
    ['José', 1500, 6],
    ['Maria', 2200, 3],
    ['Everton', 3000, 5]
]
def novosValores(salario, ano):
    novoSalario = 0
    if ano > 5:
        novoSalario = salario * 1.20
    else:
        novoSalario = salario * 1.10
    return f"{novoSalario:.2f}"

novaLista = []
def genNovaLista(lista):
    novaLista.append([lista[0], novosValores(lista[1], lista[2]), lista[2]])

for i in funcionarios:
    genNovaLista(i)

def retornarPrint():
    conteudo = ""
    for i in funcionarios:
        conteudo += f"[bold on black]Funcionario {i[0]}:[/]\nSalario antigo: [bold red]R$ {i[1]:.2f}[/]\nSalario novo: [bold green]R${novosValores(i[1], i[2])}[/]\n\n"
    tabela = Panel(conteudo, title="[ REAJUSTE VALORES ]")
    return tabela

print(retornarPrint())