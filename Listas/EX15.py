entrada = 0
lista = []

while(entrada!=-1):
    entrada = int(input("Digite a nota ou -1 para sair: "))
    if(entrada!=-1):
        lista.append(entrada)

print("Quantidade: ", len(lista))

for i in range(len(lista)):
    print(lista[i], " ", end="")

print("")

for i in range(len(lista)):
    print(lista[len(lista)-i-1])

soma = 0
media = 0

for i in range(len(lista)):
    soma+=lista[i]
    media+=lista[i]

media = media/len(lista)
print("Soma: ", soma)
print("Média: ", media)

qtdAcimaMedia = 0
qtdAbaixo7 = 0

for i in range(len(lista)):
    if(lista[i]>media):
        qtdAcimaMedia+=1
    if(lista[i]<7):
        qtdAbaixo7+=1

print("Quantidade de valores acima da média: ", qtdAcimaMedia)
print("Quantidade de valores abaixo de 7: ", qtdAbaixo7)
