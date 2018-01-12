altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))
sexo = input("M para masculino e F para feminino: ")

if(sexo=="M"):
    if(peso > ((72.7*altura)-58)):
        print("Você está acima do peso.")
    elif(peso < ((72.7*altura)-58)):
        print("Você está abaixo do peso.")
    else:
        print("Você está no peso ideal.")
else:
    if(peso > ((62.1*altura)-44.7)):
        print("Você está acima do peso.")
    elif(peso < ((62.1*altura)-44.7)):
        print("Você está abaixo do peso.")
    else:
        print("Você está no peso ideal.")
