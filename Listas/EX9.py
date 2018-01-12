lista = []

for i in range(10):
    lista.append(int(input("Digite um número: ")))

for i in range(len(lista)):
    print(lista[i]*lista[i], " ", end="")
