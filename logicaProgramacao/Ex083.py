lista = []
verificacao = []
expressao = (input("Digite uma expressao: "))
for simbolo in expressao:
    if simbolo == '(':
        verificacao.append('(')
    elif simbolo == ')':
        if len(verificacao) > 0:
            verificacao.pop()
        else:
            verificacao.append(')')
            break
if len(verificacao) == 0:
    print('Sua expressao esta correta!')
else:
    print('Sua expressao esta errada,horrivel,horrorosa,me faz mal!')