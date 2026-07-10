# Sistema de Biblioteca: Implementar clases `Libro`, `Usuario` y `Biblioteca`. La biblioteca
# debe permitir prestar libros, devolver y listar préstamos activos.

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def __str__(self):
        estado = "disponible" if self.disponible else "prestado"
        return f"{self.titulo} - {self.autor} [{estado}]"


class Usuario:
    def __init__(self, nombre): 
        self.nombre = nombre
        self.prestamos = []

    def __str__(self):
        return f"{self.nombre} ({len(self.prestamos)} libro(s) prestado(s))"


class Biblioteca:
    def __init__(self):
        self.libros = {}                 
        self.usuarios = {}
        self.prestamos = {}

    def agregarLibro(self, libro):
        self.libros[libro.titulo] = libro

    def registrarUsuario(self, usuario):
        self.usuarios[usuario.nombre] = usuario

    def prestarLibro(self, titulo, nombreUsuario):
        if titulo not in self.libros:
            print(f"El libro '{titulo}' no existe.")
            return
        if nombreUsuario not in self.usuarios:
            print(f"El usuario '{nombreUsuario}' no existe.")
            return

        libro = self.libros[titulo]

        if not libro.disponible:         
            print(f"'{titulo}' ya está prestado.")
            return

        libro.disponible = False
        self.usuarios[nombreUsuario].prestamos.append(titulo)
        self.prestamos[titulo] = nombreUsuario
        print(f"'{titulo}' prestado a {nombreUsuario}.")

    def devolverLibro(self, titulo, nombreUsuario):   
        if titulo not in self.prestamos:
            print(f"'{titulo}' no figura como prestado.")
            return
        if self.prestamos[titulo] != nombreUsuario:
            print(f"'{titulo}' fue prestado a {self.prestamos[titulo]}, no a {nombreUsuario}.")
            return

        self.libros[titulo].disponible = True         
        self.usuarios[nombreUsuario].prestamos.remove(titulo)
        del self.prestamos[titulo]
        print(f"'{titulo}' devuelto por {nombreUsuario}.")

    def listarPrestamos(self):                        
        if not self.prestamos:
            print("No hay préstamos activos.")
            return
        for titulo, nombreUsuario in self.prestamos.items():
            print(f"  {titulo} → {nombreUsuario}")



bib = Biblioteca()

bib.agregarLibro(Libro("Cien años de soledad", "García Márquez"))
bib.agregarLibro(Libro("El Quijote", "Cervantes"))
bib.agregarLibro(Libro("Harry Potter I", "J.K. Rowling"))

bib.registrarUsuario(Usuario("Ana"))
bib.registrarUsuario(Usuario("Carlos"))

bib.prestarLibro("Cien años de soledad", "Ana")
bib.prestarLibro("El Quijote", "Carlos")

bib.listarPrestamos()

bib.devolverLibro("Cien años de soledad", "Ana")

bib.listarPrestamos()