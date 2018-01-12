notas = []

i=0

for i in range(4):
    notas.append(float(input("Digite a nota: ", str(i+1))))

media = 0

for i in range(len(notas)):
    media += notas[i]
    print(notas[i], " ", end="")

print("\nSua média é: ", media/4)
