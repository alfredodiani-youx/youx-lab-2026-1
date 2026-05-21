print("Gerador de PA")
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razao: "))
i = 0
while i < 10:
    i += 1
    termo = primeiro + (i - 1) * razao
    print(f"{termo}", end= ' > ')
print("FIM")