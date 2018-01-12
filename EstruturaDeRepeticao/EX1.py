n = int(input("Digite a nota: "))

while(n<0 or n>10):
    print("Nota inválida.")
    n = int(input("Digite a nota: "))
else:
    print("Nota válida.")
