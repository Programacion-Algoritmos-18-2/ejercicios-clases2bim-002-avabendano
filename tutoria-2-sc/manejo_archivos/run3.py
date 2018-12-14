from paquete_archivos.miarchivo import MiArchivo
from paquete_modelo.mimodelo import Persona, OperacionesPersona
#Creamos un objeto de la clase MiArchivo
m = MiArchivo()
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]
# print(lista)
# Utilizamos los objetos de la lista desde su posicion 1
lista_personas =[]
lista = lista[1:]
# p = Persona(lista[1][1], lista[1][2], lista[1][3], lista[1][0])

# Creamos un for para recorrer la lista y dentro del objeto almacenamos cada linea
for d in lista:
    # print(d)
   # suma_n1 = suma_n1 + int(d[4])
    p = Persona(d[1], d[2], d[3], d[0], d[4], d[5])
    lista_personas.append(p)

#Imprimimos cada metodo que desarrollamos en nuestra clase OperacionesPersona
operaciones = OperacionesPersona(lista_personas)
print("Promedio de las notas1: ", operaciones.obtener_promedio_n1())
print("Promedio de las notas2: ",operaciones.obtener_promedio_n2())
print("Personas con notas1 menores a 15: ", operaciones.obtener_listado_n1())
print("Personas con notas2 menores a 15: ", operaciones.obtener_listado_n2())
print("Personas que empiezan con J y R: ", operaciones.obtener_listado_personas('R', 'J'))


