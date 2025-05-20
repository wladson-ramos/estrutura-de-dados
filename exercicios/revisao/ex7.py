n1 = int(input())
n2 = int(input())
soma = 0

if(n1>n2):
    print("invalido")
else:  
    for x in range(n1, n2+1):
        if x %2==0:
            soma = soma + x
    print(soma)