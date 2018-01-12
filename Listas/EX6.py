notas = []
media = []
alunosA = 0

for i in range(3):
    soma = 0
    for i in range(4):
        notas.append(float(input("Digite a nota: ")))
        soma += notas[i]
    media.append(soma/4)

for i in range(len(media)):
    if(media[i]>=7):
        alunosA+=1

print(alunosA)
