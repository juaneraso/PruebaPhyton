import json

class Configuracion:
    def __init__(self):
        self.usuarios = {}
        self.cargar_usuarios()

    def cargar_usuarios(self):
        try:
            with open("Archivos/usuarios.json", "r") as archivo:
                self.usuarios = json.load(archivo)
            print("Usuarios cargados desde el archivo usuarios.json.")
        except FileNotFoundError:
            print("No se encontró el archivo usuarios.json. No hay usuarios registrados.")

    def iniciar_sesion(self, usuario, contrasena):
        if usuario in self.usuarios and self.usuarios[usuario] == contrasena:
            print("Inicio de sesión exitoso.")
            return True
        else:
            print("Nombre de usuario o contraseña incorrectos.")
            return False

    def registrar_usuario(self, usuario, contrasena):
        if usuario not in self.usuarios:
            self.usuarios[usuario] = contrasena
            self.guardar_usuarios()
            print("Usuario registrado correctamente.")
        else:
            print("El nombre de usuario ya está en uso.")

    def guardar_usuarios(self):
        with open("Archivos/usuarios.json", "w") as archivo:
            json.dump(self.usuarios, archivo, indent=4)
        print("Usuarios guardados en el archivo usuarios.json.")

    def restablecer_contrasena(self, usuario, nueva_contrasena):
        if usuario in self.usuarios:
            self.usuarios[usuario] = nueva_contrasena
            self.guardar_usuarios()  # Guardar los cambios en el archivo
            print("Contraseña restablecida correctamente.")
        else:
            print("El usuario especificado no existe.")

    def ver_usuarios_registrados(self):
        print("Lista de usuarios registrados:")
        for usuario in self.usuarios:
            print(usuario)
