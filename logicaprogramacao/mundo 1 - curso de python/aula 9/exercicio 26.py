frase = str(input('Digite uma frase: '))
print(f"Quantas vezes a letra 'a' aparece na frase: {frase.count('a')}")
print(f"A primeira letra apareceu na posição: {frase.find('a')+1}")
print(f"A última  letra apareceu na posição: {frase.rfind('a')+1}")