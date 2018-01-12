lista = []

for i in range(10):
    lista.append(float(input("Digite um número: ")))

for i in range(len(lista)):
    print(lista[((len(lista))-i)-1]," ", end="")
