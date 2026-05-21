#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.


vogais = ("a", "e", "i", "o", "u")
tupla = ("laranja", "carro", "arcondicionado")
for palavra in tupla:
     print(f"As vogais que existem na palavra: {palavra} -> ", end="")
     for letra in palavra:
         if letra in vogais:
             print(letra, end=" ")
     print()

