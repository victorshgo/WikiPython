def data(d, m, ano):
    mes = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    if((d<=0 or d>31) or (m<1 or m>12) or (ano<0)):
        print("Valor inválido.")
    else:
        if(m==2):
            if(d>29):
                print("Valor inválido.")
            else:
                print(d, " de ", mes[m-1], " de ", ano)

d = int(input("Dia: "))
m = int(input("Mês: "))
ano = int(input("Ano: "))

data(d, m, ano)
