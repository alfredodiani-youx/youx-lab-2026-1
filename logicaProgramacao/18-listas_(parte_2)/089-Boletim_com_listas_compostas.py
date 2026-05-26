boletim =[]
escolha ="s"
mostrar = 0
c = 0
while escolha != "n":
    nome =str(input('nome: '))
    nota1 =float(input('nota 1: '))
    nota2 =float(input('nota 2: '))
    aluno =[nome, nota1, nota2]
    boletim.append(aluno)
    escolha =str(input('deseja cadastrar mais um aluno [s/n]: ')).lower()

print("-"*20)
print('No.  | Nome        | Média:')
for i,a in enumerate(boletim):
    print(f"{i:<5}",end="|")
    print(f" {a[0][:11]:<12}",end="|")
    print(f" {(a[1] + a[2]) / 2}")
while mostrar != 999:
    mostrar =int(input('mostrar as notas de qual aluno (999 para parar): '))
    if 0 <= mostrar < len(boletim):
        print(f'as notas de {boletim[mostrar][0]} sao {boletim[mostrar][1]} e {boletim[mostrar][2]}')
    else:
        print('voce digitou um numero fora da lista')   