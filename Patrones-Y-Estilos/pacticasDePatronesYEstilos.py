# =====================================================================
# 1. ESTILO ARQUITECTÓNICO: ARQUITECTURA EN CAPAS
# Dividimos conceptualmente el sistema en: Capa de Datos, Capa de Negocio 
# y Capa de Presentación. Ninguna capa hace el trabajo de la otra.
# =====================================================================


# =====================================================================
# 2. PATRÓN DE DISEÑO (Micro): SINGLETON
# Evita que creemos múltiples instancias de la base de datos por error.
# Nos asegura que toda la app comparta la misma lista de dulces.
# =====================================================================
class Database:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.dulces = [] # Simulamos la tabla de la BD
        return cls._instancia


# =====================================================================
# 3. PATRÓN ARQUITECTÓNICO (Macro): MVC (Modelo-Vista-Controlador)
# Implementa las capas separando la interfaz de la lógica y los datos.
# =====================================================================

# ---> MODELO (Capa de Datos y Reglas de Negocio)
# Solo le importa cómo guardar y validar la información. No sabe nada de "prints".
class DulceModel:
    def __init__(self):
        self.db = Database() # Usamos el patrón Singleton aquí

    def agregar(self, nombre, precio):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.db.dulces.append({"nombre": nombre, "precio": precio})

    def obtener_todos(self):
        return self.db.dulces


# ---> VISTA (Capa de Presentación)
# Su único trabajo es hablar con el usuario (consola, React, HTML). 
# No sabe cómo se guardan los datos ni cómo se validan.
class DulceView:
    def mostrar_menu(self):
        print("\n1. Agregar dulce | 2. Ver dulces | 3. Salir")
        return input("Elige: ")

    def obtener_datos_dulce(self):
        nombre = input("Nombre del dulce: ")
        precio = float(input("Precio: "))
        return nombre, precio

    def mostrar_dulces(self, dulces):
        print("\n--- Lista de Dulces ---")
        for d in dulces:
            print(f"- {d['nombre']}: ${d['precio']}")

    def mostrar_mensaje(self, mensaje):
        print(f"INFO: {mensaje}")


# ---> CONTROLADOR (Capa de Orquestación)
# Es el "director de orquesta". Toma lo que el usuario pide en la VISTA,
# le dice al MODELO qué procesar, y luego le dice a la VISTA qué mostrar.
class DulceController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def iniciar(self):
        while True:
            opcion = self.vista.mostrar_menu()
            
            if opcion == "1":
                try:
                    # 1. Pide datos a la Vista
                    nombre, precio = self.vista.obtener_datos_dulce()
                    # 2. Manda a procesar al Modelo
                    self.modelo.agregar(nombre, precio)
                    # 3. Manda respuesta a la Vista
                    self.vista.mostrar_mensaje("¡Dulce guardado con éxito!")
                except ValueError as e:
                    self.vista.mostrar_mensaje(f"ERROR: {e}")
                    
            elif opcion == "2":
                dulces = self.modelo.obtener_todos()
                self.vista.mostrar_dulces(dulces)
                
            elif opcion == "3":
                break

# =====================================================================
# EJECUCIÓN (El "Main")
# =====================================================================
if __name__ == "__main__":
    modelo = DulceModel()
    vista = DulceView()
    app = DulceController(modelo, vista)
    
    app.iniciar()