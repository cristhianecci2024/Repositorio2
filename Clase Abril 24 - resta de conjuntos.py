lista1=[15,9,10,56,78,4,6,21]
lista2=[3,5,9,4,25,21,10,13]

set1=set(lista1)
set2=set(lista2)

#set3=set1.intersection(set2)
set3=set1 - set2
lista3=list(set3)
print(lista3)