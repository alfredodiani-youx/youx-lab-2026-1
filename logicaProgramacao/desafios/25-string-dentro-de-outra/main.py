n = input("Qual seu nome?: ");
k = n.find("silva")
r = k != -1
if r == True:
    print("Seu nome tem silva");
if r != True:
    print("Seu nome não tem silva");