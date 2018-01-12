caracteres = []
consoantes = []

for i in range(10):
    letra = input("Digite uma letra: ")
    if(letra!="a" and letra!="e" and letra!="i" and letra!="o" and letra!="u"):
      consoantes.append(letra)

for i in range(len(consoantes)):
    print(consoantes[i], " ", end="")

print("\nQuantidade: ", len(consoantes))
