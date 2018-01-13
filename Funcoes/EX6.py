def converte(horas, minutos):
    print("Notação de 24h: ", horas, ":", minutos, "P.M")
    print("Notação de 12h: ", horas-12, ":", minutos, "A.M")

continuar = 1

while(continuar!=0):
    h = int(input("Digite a hora: "))
    m = int(input("Digite os minutos: "))
    converte(h, m)
    continuar = int(input("Digite 1 para continuar ou 0 para sair: "))
