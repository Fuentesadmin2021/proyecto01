## programa para saber si un número es primo
def es_primo(x):
    cont=0
    for i in range(2,x+1):
        if x%i==0:
            cont+=1
            
    if cont==1:
        return True
    return False

num=int(input())

if es_primo(num):
    print('Numero primo')
else:
    print('Este numero no es primo')

print('FIN')
print('Bye')
    