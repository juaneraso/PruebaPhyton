import json 
class Cliente:
    clientes = []

    @classmethod
    def cargar_clientes(cls):
        try:
            with open("Archivos/clientes.json", "r") as archivo:
                cls.clientes = json.load(archivo)
        except FileNotFoundError:
            cls.clientes = []

    @classmethod
    def guardar_clientes(cls):
        with open("Archivos/clientes.json", "w") as archivo:
            json.dump(cls.clientes, archivo, indent=4)

    @classmethod
    def registrar_cliente(cls, id_cliente, nombre, direccion, telefono):
        cls.clientes.append({
            "id_cliente": id_cliente,
            "nombre": nombre,
            "direccion": direccion,
            "telefono": telefono
        })
        cls.guardar_clientes()

    @classmethod
    def eliminar_cliente(cls, id_cliente):
        for cliente in cls.clientes:
            if cliente["id_cliente"] == id_cliente:
                cls.clientes.remove(cliente)
                cls.guardar_clientes()
                print(f"Cliente con ID {id_cliente} eliminado exitosamente.")
                return
        print(f"No se encontró ningún cliente con ID {id_cliente}.")

    @classmethod
    def buscar_cliente(cls, id_cliente):
        for cliente in cls.clientes:
            if cliente["id_cliente"] == id_cliente:
                return cliente
        return None

    @classmethod
    def actualizar_cliente(cls, id_cliente, nombre=None, direccion=None, telefono=None):
        cliente = cls.buscar_cliente(id_cliente)
        if cliente:
            if nombre:
                cliente["nombre"] = nombre
            if direccion:
                cliente["direccion"] = direccion
            if telefono:
                cliente["telefono"] = telefono
            cls.guardar_clientes()
            print(f"Datos del cliente con ID {id_cliente} actualizados exitosamente.")
        else:
            print(f"No se encontró ningún cliente con ID {id_cliente}.")

    @classmethod
    def ver_lista_clientes(cls):
        if cls.clientes:
            print("Lista de clientes:")
            for cliente in cls.clientes:
                print(cliente)
        else:
            print("No hay clientes registrados.")

    def __init__(self, id_cliente, nombre, direccion, telefono):
        self.__id_cliente = id_cliente
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono

    def set_id_cliente(self, id_cliente):
        self.__id_cliente = id_cliente

    def get_id_cliente(self):
       return self.__id_cliente

    def set_nombre(self, nombre):
       self.__nombre = nombre
   
    def get_nombre(self):
       return self.__nombre

    def set_direccion(self, direccion):
       self.__direccion = direccion

    def get_direccion(self):
       return self.__direccion

    def set_telefono(self, telefono):
      self.__telefono = telefono

    def get_telefono(self):
      return self.__telefono

    def __str__(self):
        return f"ID: {self.__id_cliente}, Nombre: {self.__nombre}, Dirección: {self.__direccion}, Teléfono: {self.__telefono}"

# Cargar clientes al inicio del programa
Cliente.cargar_clientes()
