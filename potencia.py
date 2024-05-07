base =  int(input("digite o valor da base: "))
expoente = int(input("digite o valor do expoente: "))
R = base
for X in range(1,expoente):
    R = R*base
print("resultado:", "{:.2f}".format(R))
