lista = []
pares = []
impar = []

for i in range(20):
    lista.append(int(input("Digite um número: ")))

for i in range(len(lista)):
    if(lista[i]%2==0):
        pares.append(lista[i])
    else:
        impar.append(lista[i])

for i in range(len(lista)):
    print(lista[i], " ", end="")

print("\n")

for i in range(len(pares)):
    print(pares[i], " ", end="")
    
print("\n")

for i in range(len(impar)):
    print(impar[i], " ", end="")
