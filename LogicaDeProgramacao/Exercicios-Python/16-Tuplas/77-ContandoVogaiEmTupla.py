for c in range(1):
    T1 = str(input('Digite uma frase: ').lower())
    for n in T1:
     if n in ('a', 'e', 'i', 'o', 'u'):
        print(f'Em {T1} as vogais são: ',end='')
        break
    for n in T1:
     if n in ('a','e','i','o','u'):
      print(n,end=' ')
      break