def imprimirNumero(numero):
    for i in range(numero+1):
        n = 1
        print("")
        while(n<=i):
            print(n, " ", end="")
            n+=1

n = int(input("Digite um número: "))
imprimirNumero(n)
