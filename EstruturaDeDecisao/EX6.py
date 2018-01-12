n1 = int(input("Digite o número 1: "))
n2 = int(input("Digite o número 2: "))
n3 = int(input("Digite o número 3: "))

if(n1>n2 and n1>n3):
    print("O maior é", n1)
elif(n2>n3):
    print("O maior é", n2)
else:
    print("O maior é", n3)
