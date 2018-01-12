idade = []
altura = []

for i in range(5):
    idade.append(int(input("Digite sua idade: ")))
    altura.append(float(input("Digite sua altura: ")))

for i in range(5):
    print("Idade: ", idade[len(idade)-i-1])
    print("Altura:", altura[len(altura)-i-1])
