nums = []
for valor in range(0, 5):
    nums.append(int(input(f'Digite o {valor+1}° valor: ')))
print(f'O maior valor digitado foi {max(nums)} e a suas posições são ', end='')
for contagem, valor in enumerate(nums):
    if valor == max(nums):
        print(contagem + 1, end='... ')
print(f'\nO menor valor digitado foi {min(nums)} e a suas posições são ', end='')
for contagem, valor in enumerate(nums):
    if valor == min(nums):
        print(contagem + 1, end='... ')