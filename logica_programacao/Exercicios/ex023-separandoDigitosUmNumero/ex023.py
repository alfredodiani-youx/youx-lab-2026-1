numero=int(input('digite um numero:'))
unidade= numero//1 % 10
dezena= numero //10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(f'unidade:{unidade} dezena: {dezena} centena: {centena} milhar: {milhar}')