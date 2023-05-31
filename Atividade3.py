#Objetivo: Criar um programa que organize uma lista de nomes em ordem alfabetica
#Bonus: Organizar por ordem alfabetica da ultima letra do nome

lista=['Alexandre','Alice','André','Arthur','Arthur','Artur','Augusto','Bernardo','Bernardo','Bruno','Davi','Diego','Eduardo','Fabrício','Felipe','Fernando','Francisco','Francisco','Gabriel','Gabriel','Giovanna','Giovanni','Guilherme','Guilherme','Hector','Henrique','Inácio','João','João','Joaquim','Júlia','Lauren','Leonardo','Leonardo','Lucas','Marina','Matheus','Matheus','Paula','Pedro','Pedro','Pedro','Pedro','Rafael','Regis','Sofia','Stella','Thiago','Valentina','Vicente','Lucas']
lista2=sorted(lista)
lista3=[]
lista5=[]
print(f'A lista, organizada em ordem alfabética é{lista2}')

#inverter os nomes
for i in range(len(lista2)):
    lista3.append(lista2[i][::-1])
lista4 = sorted(lista3) #bota em ordem alfabética os nomes invertidos

for i in range(len(lista4)):
    lista5.append(lista4[i][::-1]) #desinverte os nomes
print('\n \nEm ordem alfabética por última letra do nome a lista fica', lista5)
