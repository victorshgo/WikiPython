import random
def embaralha(palavra):
    misturar = random.sample(palavra, len(palavra))
    a = ''.join(misturar)
    return a

palavra = input("Digite uma palavra: ")
print(embaralha(palavra))
