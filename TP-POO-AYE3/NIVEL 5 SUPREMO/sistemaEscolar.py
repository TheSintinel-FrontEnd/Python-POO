# Sistema de Gestión Escolar: Crear clases para representar alumnos, profesores, materias
# y notas. Diseñar métodos para registrar calificaciones y obtener promedios.


class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = {}          # { nombre_materia: [nota1, nota2, ...] }

    def agregarNota(self, materia, nota):
        if materia not in self.notas:
            self.notas[materia] = []
        self.notas[materia].append(nota)

    def promedio(self, materia):
        if materia not in self.notas or len(self.notas[materia]) == 0:
            return 0
        return sum(self.notas[materia]) / len(self.notas[materia])

    def __str__(self):
        return f"Alumno: {self.nombre}"


class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.materias = []

    def asignarMateria(self, materia):
        self.materias.append(materia)

    def __str__(self):
        return f"Profesor: {self.nombre}"


class Materia:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
        self.alumnos = []
        profesor.asignarMateria(self.nombre)

    def inscribirAlumno(self, alumno):
        self.alumnos.append(alumno)

    def promedio(self):
        if not self.alumnos:
            return 0
        total = sum(alumno.promedio(self.nombre) for alumno in self.alumnos)
        return total / len(self.alumnos)

    def __str__(self):
        return f"Materia: {self.nombre} — Profesor: {self.profesor.nombre}"


class Escuela:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = {}
        self.profesores = {}
        self.materias = {}

    def registrarAlumno(self, alumno):
        self.alumnos[alumno.nombre] = alumno
        print(f"Alumno registrado: {alumno.nombre}")

    def registrarProfesor(self, profesor):
        self.profesores[profesor.nombre] = profesor
        print(f"Profesor registrado: {profesor.nombre}")

    def registrarMateria(self, materia):
        self.materias[materia.nombre] = materia
        print(f"Materia registrada: {materia.nombre}")

    def inscribirAlumno(self, nombre_alumno, nombre_materia):
        if nombre_alumno not in self.alumnos:
            print(f"No existe el alumno '{nombre_alumno}'.")
            return
        if nombre_materia not in self.materias:
            print(f"No existe la materia '{nombre_materia}'.")
            return
        self.materias[nombre_materia].inscribirAlumno(self.alumnos[nombre_alumno])
        print(f"{nombre_alumno} inscripto en {nombre_materia}.")

    def registrarNota(self, nombre_alumno, nombre_materia, nota):
        if nombre_alumno not in self.alumnos:
            print(f"No existe el alumno '{nombre_alumno}'.")
            return
        if nombre_materia not in self.materias:
            print(f"No existe la materia '{nombre_materia}'.")
            return
        self.alumnos[nombre_alumno].agregarNota(nombre_materia, nota)
        print(f"Nota {nota} registrada a {nombre_alumno} en {nombre_materia}.")

    def promedioAlumno(self, nombre_alumno, nombre_materia):
        if nombre_alumno not in self.alumnos:
            print(f"No existe el alumno '{nombre_alumno}'.")
            return
        promedio = self.alumnos[nombre_alumno].promedio(nombre_materia)
        print(f"Promedio de {nombre_alumno} en {nombre_materia}: {promedio:.2f}")

    def promedioMateria(self, nombre_materia):
        if nombre_materia not in self.materias:
            print(f"No existe la materia '{nombre_materia}'.")
            return
        promedio = self.materias[nombre_materia].promedio()
        print(f"Promedio general de {nombre_materia}: {promedio:.2f}")

escuela = Escuela("ISFT 190°")

# Registrar profesores y materias
prof_math = Profesor("Cadamuro")
prof_hist = Profesor("Trinchero")
escuela.registrarProfesor(prof_math)
escuela.registrarProfesor(prof_hist)

mat_math = Materia("Matemática", prof_math)
mat_hist = Materia("Historia", prof_hist)
escuela.registrarMateria(mat_math)
escuela.registrarMateria(mat_hist)

# Registrar alumnos
escuela.registrarAlumno(Alumno("Martina"))
escuela.registrarAlumno(Alumno("Eros"))

# Inscribir alumnos en materias
escuela.inscribirAlumno("Martina", "Matemática")
escuela.inscribirAlumno("Eros", "Matemática")
escuela.inscribirAlumno("Martina", "Historia")

# Cargar notas
escuela.registrarNota("Martina", "Matemática", 9)
escuela.registrarNota("Martina", "Matemática", 7)
escuela.registrarNota("Eros", "Matemática", 6)
escuela.registrarNota("Martina", "Historia", 8)

# Ver promedios
escuela.promedioAlumno("Martina", "Matemática")
escuela.promedioAlumno("Eros", "Matemática")
escuela.promedioMateria("Matemática")