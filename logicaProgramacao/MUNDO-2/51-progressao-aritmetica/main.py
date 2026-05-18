#: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#No final, mostre os 10 primeiros termos dessa progressão!

primeiro = int(input('digite o primeiro termo: '))
razao = int(input('digite a RAZAO: '))
for i in range(10):
    print(primeiro)
    segundo = primeiro + razao
    primeiro = segundo
