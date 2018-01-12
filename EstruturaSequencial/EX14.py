peso = float(input("Digite a quatidade de peixes em KG: "))
excesso = 0.0
multa = 0.0

if(peso>50):
    excesso = peso - 50
    multa = excesso*4

print("Excesso: ", excesso)
print("Multa: ", multa)
