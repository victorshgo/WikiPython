def imprimirNumero(numero):
    for i in range(numero):
        n = 1
        print("")
        while(n<=i):
            print(i, " ", end="")
            n+=1

n = int(input("Digite um número: "))
imprimirNumero(n)
