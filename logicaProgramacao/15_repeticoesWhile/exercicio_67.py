numero= int(input("qual tabuada voce quer? :"))
while True:
    if numero <0:
        break
    for tabuada in range (1, 10+1):
        print(f"{numero} x {tabuada} = {numero * tabuada}")
    break




