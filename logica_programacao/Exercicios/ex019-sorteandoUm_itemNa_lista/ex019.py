
import random
nome1 = str (input('nome do aluno:'))
nome2 = str (input('nome do aluno:'))
nome3 = str (input('nome do aluno:'))
nome4 =  str (input('nome do aluno:'))
lista = [nome1, nome2, nome3, nome4]
sorteio = random.choice(lista)
print(f'o aluno sorteado foi o {sorteio}')