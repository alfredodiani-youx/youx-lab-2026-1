opcao = 0
soma = 0
media = 0
maior = 0
menor = 0
quantidade = 0
opcao = 'S'

while opcao == 'S':
 numero = int(input("Digite um número inteiro: "))
 quantidade += 1

if quantidade == 1:
     maior = menor = numero
 else:
     if numero > maior:
         maior = numero
     if numero < menor:
         menor = numero

 opcao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
media = soma / quantidade
print(f"Você digitou {quantidade} números.")
print(f"A média foi {media:.2f}")
print(f"O maior valor foi {maior} e o menor foi {menor}")