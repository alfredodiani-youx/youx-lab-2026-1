primeiro = (int(input('Primeiro valor: ')))
segundo = int(input('Segundo valor: '))
terceiro = int(input('terceiro valor: '))

#Verificando quem é menor
if segundo < primeiro and segundo < terceiro:
    menor = segundo
if terceiro < primeiro and terceiro <segundo:
    menor = terceiro
if primeiro < segundo and primeiro < terceiro:
    menor = primeiro

#verificando quem o maior
if segundo > primeiro and segundo > terceiro:
    maior = segundo
if terceiro > primeiro and terceiro > segundo:
    maior = terceiro
if primeiro > segundo and primeiro > terceiro:
    maior = primeiro

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado fio {}'.format(maior))
