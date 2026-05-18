soma = 0
for n in range(1, 8):
    valor = int(input(f"Digite o valor {n}: "))
    soma = soma + valor
    print(f"Você escolheu {valor} e a soma parcial foi {soma}")

print(f"A soma final foi {soma}")
