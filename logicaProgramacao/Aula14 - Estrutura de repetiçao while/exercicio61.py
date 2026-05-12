#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print("Gerador de PA")
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razao: "))
i = 0
while i < 10:
    i += 1
    termo = primeiro + (i - 1) * razao
    print(f"{termo}", end= ' > ')
print("FIM")