v = float(input('Qual é o valor da casa? '))
s = float(input('Qual é o seu salario? '))
t = int(input('Em quantos anos pretende pagar? '))
if v / (t * 12) <= s * 30/100:
    print(f'O emprestimo foi aprovado, o valor da parcela sera {v / (t * 12):.2f}')
elif v / (t * 12 > s * 30/100):
    print('O emprestimo foi negado, a parcela excede o limte permitido')