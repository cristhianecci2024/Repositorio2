lista_estudiantes=["andres","cristian","gary","stiven","felipe"]
lista_calificaciones=[3.4,2.0,1.0,1.5,4.8]
materias=["pc","cc","eb","ge","pb"]
#estudiante=input("Nombre del estudiante\n")
#cuenta=1
#indice=0
#persona=estudiante
#posicion=-1

def buscar (persona,lista):
    for i, nombre in  enumerate(lista):
        if  nombre==persona:
            return i
    return -1

estudiante=input("Nombre del estudiante\n")
pos=buscar(estudiante,lista_estudiantes)
nota=lista_calificaciones[pos]
mat=materias[pos]
print(estudiante,"Saco",nota,"en",mat)