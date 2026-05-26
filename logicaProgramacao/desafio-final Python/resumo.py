# =========================
# LISTAS EM PYTHON
# =========================

# Lista guarda vários valores

frutas = ["maçã", "banana", "uva"]

print(frutas)

# Pegando item da lista
print(frutas[0])

# Alterando item
frutas[1] = "morango"

print(frutas)

# Adicionando item
frutas.append("laranja")

print(frutas)

# Removendo item
frutas.remove("uva")

print(frutas)

# Tamanho da lista
print(len(frutas))


# =========================
# EXEMPLO COMPLETO DE LISTA
# =========================

nomes = []

nomes.append("Ana")
nomes.append("Carlos")
nomes.append("Julia")

print(nomes)

print("Primeiro nome:", nomes[0])

nomes.remove("Carlos")

print("Lista final:", nomes)


# =========================
# DICIONÁRIOS EM PYTHON
# =========================

# Dicionário guarda chave e valor

pessoa = {
    "nome": "Ana",
    "idade": 18,
    "cidade": "Lavras"
}

print(pessoa)

# Pegando valor
print(pessoa["nome"])

# Alterando valor
pessoa["idade"] = 19

# Adicionando informação
pessoa["altura"] = 1.65

# Removendo informação
del pessoa["cidade"]

print(pessoa)


# =========================
# EXEMPLO COMPLETO DE DICIONÁRIO
# =========================

aluno = {
    "nome": "Pedro",
    "nota": 8.5,
    "aprovado": True
}

print(aluno["nome"])

aluno["nota"] = 9

aluno["turma"] = "2A"

print(aluno)


# =========================
# FOR EM PYTHON
# =========================

# Repetição usando range

for i in range(5):
    print(i)

# Outro exemplo

for numero in range(1, 6):
    print(numero)


# =========================
# FOR COM LISTA
# =========================

frutas = ["maçã", "banana", "uva"]

for fruta in frutas:
    print(fruta)


# =========================
# FOR COM DICIONÁRIO
# =========================

pessoa = {
    "nome": "Ana",
    "idade": 18
}

# Mostra as chaves

for chave in pessoa:
    print(chave)

# Mostra chave e valor

for chave, valor in pessoa.items():
    print(chave, valor)


# =========================
# JUNTANDO TUDO
# =========================

alunos = [
    {"nome": "Ana", "nota": 8},
    {"nome": "Carlos", "nota": 6},
    {"nome": "Julia", "nota": 10}
]

for aluno in alunos:
    print(aluno["nome"])
    print(aluno["nota"])
