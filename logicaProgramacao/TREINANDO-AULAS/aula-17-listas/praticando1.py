num = [1, 3, 8, 9]

num[0] = 6

num.append(10) #adiciona o valor 10

num.sort()
print(num)

num.insert(3, 7) #adiciona um valor na posiçao 3

num.pop(2)  #remove um numero da posiçao 2

num.sort(reverse=True)
print(num)    #coloca os numeros em ordem

num.remove(9)

print(f'essa lista tem {len(num)} elementos')  #LEN retorna quantos elementos tem