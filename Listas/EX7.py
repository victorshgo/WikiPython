lista = []
soma = 0
mult = 1

for i in range(5):
    lista.append(int(input("Digite um número: ")))
    soma+=lista[i]
    mult*=lista[i]

print(soma)
print(mult)

for i in range(len(lista)):
    print(lista[i], " ", end="")
