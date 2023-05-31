#Objetivo: Criar um programa que printe os numeros de uma lista e, depois, eles multiplicados por 2
#Bonus: Colocar os numeros multiplicados em uma outra lista e printa-la


lista=[2,3,7,12,2]
lista2=[]
for i in range(len(lista)):
    print(f'O numero {lista[i]} vezes 2 é {lista[i]*2}')
    lista2.append(lista[i]*2)
print(lista2)
