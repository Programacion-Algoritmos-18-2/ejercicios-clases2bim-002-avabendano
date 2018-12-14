"""
    creación de clases
"""

class Persona(object):
    """
    """
    
    def __init__(self, n, ape, ed, cod, not1, not2):
        """
        """
        self.nombre = n
        self.edad = int(ed)
        self.codigo = int(cod)
        self.apellido = ape
        self.nota_1 = int(not1)
        self.nota_2 = int(not2)

    def agregar_nombre(self, n):
        """
        """
        self.nombre = n

    def obtener_nombre(self):
        """
        """
        return self.nombre

    def agregar_edad(self, n):
        """
        """
        self.edad = int(n)

    def obtener_edad(self):
        """
        """
        return self.edad
    
    def agregar_codigo(self, n):
        """
        """
        self.codigo = int(n)

    def obtener_codigo(self):
        """
        """
        return self.codigo
    
    def obtener_apellido(self):
        """
        """
        return self.apellido

    def agregar_nota_1(self, not1):
        self.nota_1 = int(not1)

    def obtener_nota_1(self):
        return self.nota_1

    def agregar_nota_2(self, not2):
        self.nota_2 = int(not2)

    def obtener_nota_2(self):
        return self.nota_2

    def __str__(self):
        """
        """
        return "%s - %s - %d - %d - %d - %d" % (self.nombre, self.apellido,\
                self.edad, self.codigo, self.nota_1, self.obtener_nota_2())


class OperacionesPersona(object):
    """
    """
    
    def __init__(self, listado):
        """
        """
        self.listado_personas = listado

    # Obtener el promedio de notas1
    def obtener_promedio_n1(self):
        suma = 0
        for n in self.listado_personas:
            # Se Suma iterativamente las notas1
            suma = suma + n.obtener_nota_1()
        # Se calcula el promedio dividiendo la suma / la longitud de la lista
        promedio = suma/len(self.listado_personas)
        return promedio

    # Obtener el promedio de notas2
    def obtener_promedio_n2(self):
        suma = 0
        for n in self.listado_personas:
            # Se Suma iterativamente las notas2
            suma = suma + n.obtener_nota_2()
        # Se calcula el promedio dividiendo la suma / la longitud de la lista
        promedio = suma / len(self.listado_personas)
        return promedio

    # Obtener las personas con notas1 < 15
    def obtener_listado_n1(self):
        nombre = ""
        for n in self.listado_personas:
            # Si en la lista las notas1 son menores a 15 entonces
            if (n.obtener_nota_1() < 15):
                # Se acumulan los nombres de las personas con notas1 < 15
                nombre = nombre + n.obtener_nombre()
        return nombre

    # Obtener las personas con notas2 < 15
    def obtener_listado_n2(self):
        nombre = ""
        for n in self.listado_personas:
            # Si en la lista las notas1 son menores a 15 entonces
            if (n.obtener_nota_2() < 15):
                # Se acumulan los nombres de las personas con notas1 < 15
                nombre = nombre + n.obtener_nombre()
        return nombre

    # Obtener las personas que empiezen su nombre con R o J
    def obtener_listado_personas(self, c1, c2):
        nombre = ""
        for n in self.listado_personas:
            # Si al obtener los nombres de las personas en la prosicion[0]
            # que equivale al primer caracter son iguales a los caracteres
            # que necesita el usuario entonces
            if (n.obtener_nombre()[0] == c1 or n.obtener_nombre()[0] == c2):
                # Acumulo los nombres de personas que empiezan con los caracteres que necesita el usuario
                # para el ejercicio envio R y J
                nombre = nombre + n.obtener_nombre() + " "

        return nombre

    def __str__(self):
        """"""
        cadena = ""
        for n in self.listado_personas:
            #cadena = "%s- %s- %s -%d\n" %(cadena , n.obtener_nombre(), n.obtener_apellido())
            cadena = "%d" %(self.obtener_promedio_n1())
            cadena = "%d" %(self.obtener_promedio_n2())
            cadena = "%d" %(self.obtener_listado_n1())
            cadena = "%d" %(self.obtener_listado_n2())
            cadena = "%d" %(self.obtener_listado_personas())
            #print(n)
        return cadena

