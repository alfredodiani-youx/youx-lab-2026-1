#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual
# foi o maior e o menor valor digitado e as suas respectivas posições na lista.


lista_numero = []
for c in range(0,5):
   lista_numero.append(int(input(f"Digite um valor para a posição {c}: ")))
   if c == 0:
      maior = menor = lista_numero[c]
   else:
      if maior > lista_numero[c]:
         lista_numero[c] = maior
      if menor < lista_numero[c]:
         lista_numero[c] = menor
print(f"Voce digitou os valores {lista_numero[c]}")
print(f"O maior valor digitado foi {maior} e o menor valor digitado foi {menor}")
