pri=int(input('Primeiro termo: '))
seg=int(input('Razão: '))
#dec=(pri+pri)+pri
#dec =int(((pri+seg)*2*10)/seg)-0
dec= pri+(10 - 1)*seg + seg
print(dec)
for c in range (pri,dec,seg):
    print(c)