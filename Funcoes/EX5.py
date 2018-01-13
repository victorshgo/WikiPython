def somaImposto(taxaImposto, custo):
    custo = custo + (custo/100*taxaImposto)
    return custo

print(somaImposto(10, 100))
