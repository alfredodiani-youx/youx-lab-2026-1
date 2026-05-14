n=int(input ('Quanto km a viagem tem? '))
n1=n*0.50
n2=n*0.45
if n <= 200:
    print (f'a passagem custara {n1} reais.')
else:
    print (f'A passagem custara {n2} reais.')