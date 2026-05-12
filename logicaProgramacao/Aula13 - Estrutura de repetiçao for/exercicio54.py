#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

maior = 0
menor = 0
for p in range (1 , 7 + 1):
   ano = int(input("Digite o ano do seu nascimento: "))
   idade = 2026 - ano
   if idade >= 18:
       maior += 1
   else:
       menor += 1
print(f"{maior} pessoas sao maiores de idade e {menor} pessoas sao menores de idade")