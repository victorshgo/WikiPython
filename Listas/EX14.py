perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]
classificacao = 0

for i in range(len(perguntas)):
    print(perguntas[i])
    resposta = input("S para sim ou N para não: ")
    if(resposta=="S"):
        classificacao+=1

if(classificacao==2):
    print("Suspeita.")
elif(classificacao==3 or classificacao==4):
    print("Cúmplice.")
elif(classificacao==5):
    print("Assassino.")
else:
    print("Inocente.")
