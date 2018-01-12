salarioHora = float(input("Digite quanto você ganha por hora: "))
horasTrabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

salario = salarioHora*horasTrabalhadas

impostoRenda = 11/100*salario
inss = 8/100*salario
sindicato = 5/100*salario

print("Sálario bruto: R$", salario)
print("Imposto de renda (11%): R$", impostoRenda)
print("INSS (8%): R$", inss)
print("Sindicato (5%): R$", sindicato)
print("Sálario líquido: R$", salario-impostoRenda-inss-sindicato)
