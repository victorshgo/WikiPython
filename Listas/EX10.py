listaA = []
listaB = []
listaC = []

for i in range(10):
    listaA.append(int(input("Digite um número para a lista A: ")))
    listaB.append(int(input("Digite um número para a lista B: ")))

for i in range(10):
    listaC.append(listaA[i])
    listaC.append(listaB[i])

for i in range(20):
    print(listaC[i], " ", end="")
