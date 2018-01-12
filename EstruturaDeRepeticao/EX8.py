lista = []
soma = 0

for i in range(5):
    lista.append(int(input("N°: ")))
    soma += lista[i]

media = soma/5

print("A soma é: ", soma)
print("A média é: ", media)
