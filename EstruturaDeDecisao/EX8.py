p1 = float(input("Digite o preço 1: "))
p2 = float(input("Digite o preço 2: "))
p3 = float(input("Digite o preço 3: "))

if(p1<p2 and p1<p3):
    print("O menor é", p1)
elif(p2<p3):
    print("O menor é", p2)
else:
    print("O menor é", p3)
