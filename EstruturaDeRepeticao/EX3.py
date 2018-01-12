nome = ""
idade = 0
salario = 0
sexo = ""
estadoCivil = ""

while (len(nome)<=3):
  nome = input("Nome: (Com mais de 3 letras) ")

while (idade < 0 or idade > 150):
  idade = input("Idade:(Entre 0 e 150) ")

while (salario <= 0):
  salario = int(input("Salário: (Maior que 0) "))

while (sexo != "F"  and sexo != "M"):
  sexo = input("Sexo: [M/F] ")

while (estadoCivil != "S" and estadoCivil != "C" and estadoCivil != "V" and estadoCivil != "D"):
  estadoCivil = input("Estado Civil: [S/C/V/D] ")
    
