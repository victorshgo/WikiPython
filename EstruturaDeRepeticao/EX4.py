paisA = 80000
paisB = 200000
taxaA = 3
taxaB = 1.5
anos  = 0

while(paisA<paisB):
    anos  += 1
    paisA += (taxaA/100*paisA)
    paisB += (taxaB/100*paisB)

print("Anos: ", anos)
