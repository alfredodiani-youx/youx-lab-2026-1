l = []
l1 = []
l2 = []
l3 = []

o = 0

while o != 9:
    if o <= 2:
        l1.append(int(input(f"Digite o número linha [0, {o}]: ")))

    if o > 2 and o <= 5:
        l2.append(int(input(f"Digite o número linha [1, {o-3}]: ")))

    if o > 5:
        l3.append(int(input(f"Digite o número linha [2, {o-6}]: ")))

    o += 1

l.append(l1)
l.append(l2)
l.append(l3)

print("=>"*30)
for i in l:
    print(f"[ {i[0]} ]  [ {i[1]} ]  [ {i[2]} ]")