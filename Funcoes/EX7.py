def valorPagamento(valorPrestacao, atraso):
    valor = valorPrestacao + (valorPrestacao/100*3) + (valorPrestacao/100*(atraso/100*1))
    return valor

valorPrestacao = 1
valorTotal = 0
prestacoes = 0

while(valorPrestacao!=0):
    valorPrestacao = float(input("Digite o valor da prestação: "))
    atraso = int(input("Dias em atraso: "))
    valorTotal += valorPagamento(valorPrestacao, atraso)
    prestacoes += 1

print("Quantidade: ", prestacoes)
print("Valor total: ", valorTotal)
