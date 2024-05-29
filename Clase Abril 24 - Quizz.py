lista1=[15,9,10,56,78,4,6,21]
lista2=[3,5,9,4,25,21,10,13]
lista3=[]

for element1 in lista1:
    for element2 in lista2:
        if element1==element2:
            lista3+=[element2]
print(lista3)