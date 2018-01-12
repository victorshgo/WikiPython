numero = int(input("Digite um número: "))
divisor = 2
cont = 0

while(divisor<=numero):
    if(numero%divisor==0):
        cont+=1
    if(cont>1):
        break
    divisor+=1

if(cont==1):
    print("É primo!")
else:
    print("Não é primo!")
    
