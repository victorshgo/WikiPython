i = 0
pares = 0
impares = 0

while(i<10):
    n = int(input("Digite um número: "))
    if(n%2==0):
        pares+=1
    else:
        impares+=1
    i+=1

print("Pares: ", pares)
print("Impares: ", impares)
