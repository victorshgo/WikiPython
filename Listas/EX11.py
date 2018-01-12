listaA = []
listaB = []
listaC = []
listaD = []

for i in range(10):
    listaA.append(int(input("Digite um número para a lista A: ")))
    listaB.append(int(input("Digite um número para a lista B: ")))
    listaC.append(int(input("Digite um número para a lista C: ")))

for i in range(10):
    listaD.append(listaA[i])
    listaD.append(listaB[i])
    listaD.append(listaC[i])

for i in range(30):
    print(listaD[i], " ", end="")
