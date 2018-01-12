base = int(input("Digite a base: "))
expo = int(input("Digite o expoente: "))
resultado = base

for i in range(expo-1):
    resultado*=base

print(resultado)
