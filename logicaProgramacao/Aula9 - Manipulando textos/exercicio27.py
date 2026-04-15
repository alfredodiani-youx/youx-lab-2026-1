#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input("Digite seu nome: ").strip()
print(f"Bem vindo {nome}")
lista = nome.split
print("")
print(f"Seu ultimo nome é {nome[len(lista)-1]}")