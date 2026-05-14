p1=float(input('Qual o peso? R: '))
p2=float(input('Qual p peso? R: '))
p3=float(input('Qual o peso? R:: '))
p4=float(input('Qual o peso? R: '))
p5=float(input('Qual o peso? R: '))
if p1 > p2 and p1 > p3 and p1 > p4 and p1 > p5:
    print(f'O maior peso foi {p1} kilos!')
elif p2 > p1 and p2 > p3 and p2 > p4 and p2 > p5:
    print(f'O maior peso foi {p2} kilos!')
elif p3 > p1 and p3 > p2 and p3 > p4 and p3 > p5:
    print(f'O maior peso foi {p3} kilos!')
elif p4 > p1 and p4 > p2 and p4 > p3 and p4 > p5:
    print(f'O maior peso foi {p4} kilos!')
elif p5 > p1 and p5 > p2 and p5 > p3 and p5 > p4:
    print(f'O maior peso foi {p5} kilos')
if p1 < p2 and p1 < p3 and p1 < p4 and p1 < p5:
    print(f'O menor peso foi {p1} kilos!')
elif p2 < p1 and p2 < p3 and p2 < p4 and p2 < p5:
    print(f'O menor peso foi {p2} kilos!')
elif p3 < p1 and p3 < p2 and p3 < p4 and p3 < p5:
    print(f'O menor peso foi {p3}')
elif p4 < p1 and p4 < p2 and p4 < p3 and p4 < p5:
    print(f'O menor peso foi {p4} kilos!')
elif p5 < p1 and p5 < p2 and p5 < p3 and p5 < p4:
    print(f'O menor peso foi {p5} kilos!')
else:
    print('Alguns tem o mesmo peso')