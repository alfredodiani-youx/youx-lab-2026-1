#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*num):
    print("Analisando...")
    c = len(num)
    print(f"{num}. Foram informados {c} numeros")
    print(f"O maior numero foi {max(num)}")
maior(4, 5, 102, 6, 71, 3)
maior(10, 7, 4, 3, 93)
maior(2, 4 ,1, -4, 4 )