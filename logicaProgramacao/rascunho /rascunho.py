funcionarios = [
    {"Nome": "José", "Salario": 1500, "anos_trabalhados": 6},
    {"Nome": "Maria", "Salario": 2200, "anos_trabalhados": 3},
    {"Nome": "Carlos", "Salario": 3000, "anos_trabalhados": 8}
]

for funcionario in funcionarios:

    if funcionario["anos_trabalhados"] > 5:
        novo_salario = funcionario["Salario"] * 1.20
    else:
        novo_salario = funcionario["Salario"] * 1.10

    funcionario["novo_salario"] = novo_salario