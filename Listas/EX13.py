mesL = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
mesN = []
media = 0
for i in range(12):
    mesN.append(float(input("Temperatura média do mês " + str(i+1) + ": ")))
    media+=mesN[i]

media = media/len(mesN)
print("A temperatura anual é: ", media)

for i in range(len(mesN)):
    if(mesN[i]>media):
        print(mesN[i], " - ", mesL[i])
