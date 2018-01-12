n1 = int(input("Digite o número 1: "))
n2 = int(input("Digite o número 2: "))
n3 = int(input("Digite o número 3: "))

if(n1>n2 and n1>n3):
    if(n2>n3):
        print("Ordenado:", n1, ",", n2 , ",", n3)
    else:
        print("Ordenado:", n1, ",", n3 , ",", n2)
elif(n2>n3):
    if(n1>n3):
        print("Ordenado", n2, ",", n1 , ",", n3)
    else:
        print("Ordenado:", n2, ",", n3 , ",", n1)
else:
    if(n1>n2):
        print("Ordenado:", n3, ",", n1 , ",", n2)
    else:
        print("Ordenado:", n3, ",", n2 , ",", n1)
