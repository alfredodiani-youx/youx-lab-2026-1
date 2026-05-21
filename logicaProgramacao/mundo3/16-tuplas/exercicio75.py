numero = (int(input("Digite um numero:")),
          int(input("Digite mais um numero: ")),
          int(input("Digite outro numero: ")),
          int(input("Digite o ultimo numero: ")))
print(f"Voce digitou esses numeros {numero}")
print(f"O numero 9 apareceu {numero.count(9)} vezes")
print(f"O primeiro valor 3 foi digitado na {numero.index(3)+1} posiçao ")
for n in numero:
    if n % 2 ==0:
       print(f"Foi digitado {n} numeros par" , end= ' ')