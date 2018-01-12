a = 0
b = 1

n = int(input("N°: "))

for i in range(n-1):
    print(b)
    b += a;
    a = b - a;
