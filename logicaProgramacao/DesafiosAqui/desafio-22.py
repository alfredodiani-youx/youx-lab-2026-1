from itertools import count

a = str(input('digite seu nome completo: '))
n1 = a.upper ()
n2 = a.lower()
n3 = a.strip()
n4 =  len(a)
n5 = a.split()[0]
n6 = len(n5)
n7 = a.split()
n8 = a.count(' ')
n9 = (n4 - n8)
print("""O nome em maiúsculo é: {}
e em minusculo é: {}
quantidade de letras no  primeiro nome: {}
quantidade de letras ao todo: {}.""".format(n1,n2,n6,n9))
