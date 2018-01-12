idade = []
altura = []
media = 0
qtd = 0

for i in range(3):
    idade.append(int(input("Digite sua idade: ")))
    altura.append(float(input("Digite sua altura: ")))
    media+=altura[i]

media = media/len(altura)

for i in range(3):
    if(idade[i]>13 and altura[i]<media):
        qtd+=1

print(qtd)
