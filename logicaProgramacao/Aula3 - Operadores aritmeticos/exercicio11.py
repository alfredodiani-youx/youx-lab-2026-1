#Crie um codigo que leia a altura e largura de uma parede e logo em seguida mostre sua area e quantos
#litros de tinta seria necessario para pintar a parede.
altura = float(input("Digite a altura da parede: "))
largura = float(input("Digite a largura da parede: "))
area = altura * largura
tinta = area / 2
print(f"Sua parede tem a dimensao de {altura}X{largura} e sua area é de {area}m2    ")
print(f"Para pintar essa parede, voce precisara de {tinta} litros de tinta para pintar essa parede.")