paisA = 0
paisB = 0
taxaA = 0
taxaB = 0
anos  = 0

while(paisA<1):
    paisA = int(input("Habitantes do país A: "))
                
while(paisB<1):
    paisB = int(input("Habitantes do país B: "))

while(taxaA<=0):
    taxaA = float(input("Taxa de crescimento do país A: "))
    
while(taxaB<=0):
    taxaB = float(input("Taxa de crescimento do país B: "))
                
while(paisA<paisB):
    anos  += 1
    paisA += (taxaA/100*paisA)
    paisB += (taxaB/100*paisB)

print("Anos: ", anos)
