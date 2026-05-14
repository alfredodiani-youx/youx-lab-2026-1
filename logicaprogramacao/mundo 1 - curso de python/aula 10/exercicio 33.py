numero1: int = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))

if numero1 > numero3 and numero1 > numero2:
    print(f"O número {numero1} é o maior!")
if numero2 > numero1 and numero2 > numero3:
    print(f"O número {numero2} é o maior!")
if numero3 > numero2 and numero3 > numero1:
    print(f"O número {numero3} é o maior!")

if numero1 < numero3 and numero1 < numero2:
    print(f"O número {numero1} é o menor!")
if numero2 < numero1 and numero2 < numero3:
    print(f"O número {numero2} é o menor!")
if numero3 < numero2 and numero3 < numero1:
    print(f"O número {numero3} é o menor!")