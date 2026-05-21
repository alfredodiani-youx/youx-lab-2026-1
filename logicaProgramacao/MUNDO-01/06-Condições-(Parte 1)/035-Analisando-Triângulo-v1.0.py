print('-='*20)
print('analisador de triangulos')
print('-='*20)
r1 = float(input('primeiro seguimento: '))
r2 = float(input('segundo seguimentp: '))
r3 = float(input('terceiro seguimento: '))
if r1 >= r2 + r3 or r2 >= r1 + r3 or r3 >= r1 + r2:
    pass
else:
