lista_estudiantes=["andres","cristian","gary","stiven","felipe"]
lista_calificaciones=[3.4,2.0,1.0,1.5,4.8]
materias=["pc","cc","eb","ge","pb"]
estudiante=input("Nombre del estudiante\n")
cuenta=1
indice=0
persona=estudiante
posicion=-1

for i in range(len(lista_estudiantes)):
    #print(i,lista_estudiantes[i])
    if  persona==lista_estudiantes[i]:
      #  print("Encontrado")
        posicion=i
print("Encontrado:",posicion)