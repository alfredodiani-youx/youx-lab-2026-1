import random
pri=int(input('Primeiro valor: '))
seg=int(input('Segundo valor: '))
ter=int(input('terceiro valor:  '))
if pri<seg and pri<ter:
    menor =  pri
if seg<pri and seg<ter:
    menor = seg
if ter<seg and ter <pri:
    menor=ter
if pri>seg and pri>ter:
    maior= pri
if seg>pri and seg> ter:
    maior=seg
if ter>pri and ter>seg:
    maior=ter
print(f'O menor valor é {menor}')
print(f'O mair valor é {maior}')