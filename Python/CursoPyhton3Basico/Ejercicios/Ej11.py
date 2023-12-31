#factorial de un numero

n=int(input("Dime un numero:"))
factorial=1

while(n!=0):
    factorial*=n
    n-=1

print("Factorial:"+str(factorial))