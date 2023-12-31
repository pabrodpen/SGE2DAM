#tabla de multiplicar de un numero

n=int(input("Dime un numero:"))

for i in range(1,11):
    print(str(n)+"x"+str(i)+"="+str(n*i))