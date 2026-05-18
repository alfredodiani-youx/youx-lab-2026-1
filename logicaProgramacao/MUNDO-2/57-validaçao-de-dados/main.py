#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input("digite se o sexo é [M/F]: ").lower()
while sexo not in 'm,f':
    print('esta incorreto,digite novamente')
    sexo = input("digite se o sexo é [M/F]: ").lower()
print('FIM')




