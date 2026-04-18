n = int(input("Digite um valor ou use [999] para sair:"))
to = n
co = 1
while n != 999:
    n = int(input("Digite outro valor use [999] para sair: "))
    if n != 999:
        to += n
        co += 1
print("você digitou {} números e a soma entre eles foi {}".format(co, to))