class Libro:
    def __init__(self, titulo, editorial, autor):
        self.titulo = titulo
        self.editorial = editorial
        self.autor = autor
        self.disponibilidad = True

    def __str__(self):
        return f"{self.titulo} por {self.autor}"

    def prestar(self):
        if self.disponibilidad:
            self.disponibilidad = False
            return True
        else:
            return False

    def devolver(self):
        self.disponibilidad = True


class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f"{self.nombre} ({self.nacionalidad})"


class Usuario:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id
        self.libros_prestados = []

    def tomar_prestado(self, libro):
        if libro.prestar():
            self.libros_prestados.append(libro)
            print(f"Libro '{libro.titulo}' prestado a {self.nombre}")
        else:
            print(f"El libro '{libro.titulo}' no esta disponible")

    def devolver_libros(self, libro):
        if libro in self.libros_prestados:
            libro.devolver()
            self.libros_prestados.remove(libro)
            print(f"Libro '{libro.titulo}' devuelto con exito por {self.nombre} con ID {self.id}")
        else:
            print(f"{self.nombre} no tiene prestado '{libro.titulo}'")


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro agregado: {libro}")

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuario registrado: {usuario.nombre} (ID {usuario.id})")

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if titulo.lower() in libro.titulo.lower():
                estado = "disponible" if libro.disponibilidad else "prestado"
                print(f"Encontrado: {libro} - {estado}")
                return libro
        print(f"No se encontro ningun libro con '{titulo}'")
        return None


"""_summary_ Diseño de sistema
    Class: Libro, Autor, Usuario y Biblioteca
    Metodos: Agregar libros, prestarlos, devolverlos y buscar
"""

# Pruebas
biblioteca = Biblioteca()

autor1 = Autor("Gabriel Garcia Marquez", "Colombiano")
libro1 = Libro("Cien años de soledad", "Patito", autor1)
libro2 = Libro("El amor en los tiempos del colera", "Patito", autor1)

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

usuario1 = Usuario("Ana", 1)
usuario2 = Usuario("Luis", 2)
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

print()
usuario1.tomar_prestado(libro1)
usuario2.tomar_prestado(libro1)      # no disponible
biblioteca.buscar_libro("cien")

print()
usuario1.devolver_libros(libro1)
usuario2.tomar_prestado(libro1)      # ahora si
usuario1.devolver_libros(libro2)     # Ana no lo tiene
biblioteca.buscar_libro("Rayuela")   # no existe