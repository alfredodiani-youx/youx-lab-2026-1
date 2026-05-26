funcionarios =[ {"Nome": "José", "Salario": 1500, "anos_trabalhados": 6},
    {"Nome": "Maria", "Salario": 1800, "anos_trabalhados": 4},
    {"Nome": "João", "Salario": 2200, "anos_trabalhados": 8},
    {"Nome": "Ana", "Salario": 2000, "anos_trabalhados": 3},
    {"Nome": "Carlos", "Salario": 2500, "anos_trabalhados": 10},
    {"Nome": "Paula", "Salario": 2300, "anos_trabalhados": 5},
    {"Nome": "Marcos", "Salario": 1900, "anos_trabalhados": 2},
    {"Nome": "Fernanda", "Salario": 2600, "anos_trabalhados": 7},
    {"Nome": "Rafael", "Salario": 2100, "anos_trabalhados": 4},
    {"Nome": "Clara", "Salario": 2400, "anos_trabalhados": 6},
    {"Nome": "Bruno", "Salario": 1700, "anos_trabalhados": 1},
    {"Nome": "Luiza", "Salario": 2800, "anos_trabalhados": 9},
    {"Nome": "Felipe", "Salario": 1950, "anos_trabalhados": 3},
    {"Nome": "Camila", "Salario": 2250, "anos_trabalhados": 5},
    {"Nome": "Ricardo", "Salario": 2700, "anos_trabalhados": 11},
    {"Nome": "Patrícia", "Salario": 2100, "anos_trabalhados": 4},
    {"Nome": "Gustavo", "Salario": 2600, "anos_trabalhados": 8},
    {"Nome": "Larissa", "Salario": 1850, "anos_trabalhados": 2},
    {"Nome": "Tiago", "Salario": 2350, "anos_trabalhados": 6},
    {"Nome": "Renata", "Salario": 2550, "anos_trabalhados": 7},
    {"Nome": "Diego", "Salario": 2000, "anos_trabalhados": 3},
    {"Nome": "Beatriz", "Salario": 2450, "anos_trabalhados": 5},
    {"Nome": "André", "Salario": 1900, "anos_trabalhados": 2},
    {"Nome": "Aline", "Salario": 2300, "anos_trabalhados": 4},
    {"Nome": "Fábio", "Salario": 2750, "anos_trabalhados": 9},
    {"Nome": "Sofia", "Salario": 2150, "anos_trabalhados": 3},
    {"Nome": "Eduardo", "Salario": 2650, "anos_trabalhados": 8},
    {"Nome": "Carolina", "Salario": 2050, "anos_trabalhados": 4},
    {"Nome": "Henrique", "Salario": 2500, "anos_trabalhados": 6},]

maiorde5 = dict()
maiorde5Lista = []
menorDe5 = dict()
menorDe5Lista = []
for a in funcionarios:
    if a["anos_trabalhados"] > 5:
        maiorde5.clear()
        maiorde5['Funcionario'] = a["Nome"]
        maiorde5['Salario Antigo'] = a["Salario"]
        novoMaior = a["Salario"] + (a["Salario"] * 20 / 100)
        maiorde5['Salario Novo'] = novoMaior
        maiorde5Lista.append(maiorde5.copy())
    elif a["anos_trabalhados"] <= 5:
        menorDe5.clear()
        menorDe5['Funcionario'] = a["Nome"]
        menorDe5['Salario Antigo'] = a["Salario"]
        novoMenor = a["Salario"] + (a["Salario"] * 10 / 100)
        menorDe5['Salario Novo'] = novoMenor
        menorDe5Lista.append(menorDe5.copy())
print('==============> Lista De Funcionarios <==============')
print('   Funcionarios com mais de 5 anos na empresa:')
for a in maiorde5Lista:
    print(f'Funcionario {a['Funcionario']}: Salario Antigo: {a['Salario Antigo']} Salario Novo: {a['Salario Novo']}')
print('   Funcionarios com 5 anos ou menos na empresa:')
for a in menorDe5Lista:
    print(f'Funcionario {a['Funcionario']}: Salario Antigo: {a['Salario Antigo']} Salario Novo: {a['Salario Novo']}')





