lista = []
maior = 0

for i in range(5):
    lista.append(int(input("N°: ")))
    if(maior<lista[i]):
        maior = lista[i]

print("O maior é: ", maior)
