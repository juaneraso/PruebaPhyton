import json

class Inventario:
    inventarios = []

    def __init__(self, id_inventario, producto_id, cantidad, ubicacion):
        self.__id_inventario = id_inventario
        self.__producto_id = producto_id
        self.__cantidad = cantidad
        self.__ubicacion = ubicacion
        Inventario.inventarios.append(self)

    # Métodos para establecer y obtener los atributos del inventario
    def set_id_inventario(self, id_inventario):
        self.__id_inventario = id_inventario

    def get_id_inventario(self):
        return self.__id_inventario

    def set_producto_id(self, producto_id):
        self.__producto_id = producto_id

    def get_producto_id(self):
        return self.__producto_id

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def get_cantidad(self):
        return self.__cantidad

    def set_ubicacion(self, ubicacion):
        self.__ubicacion = ubicacion

    def get_ubicacion(self):
        return self.__ubicacion

    # Método para imprimir la información del inventario
    def __str__(self):
        return f"ID de Inventario: {self.__id_inventario}, ID de Producto: {self.__producto_id}, Cantidad: {self.__cantidad}, Ubicación: {self.__ubicacion}"

    # Método para agregar cantidad al inventario
    def agregar_cantidad(self, cantidad):
        self.__cantidad += cantidad

    # Método para restar cantidad al inventario
    def restar_cantidad(self, cantidad):
        if self.__cantidad >= cantidad:
            self.__cantidad -= cantidad
        else:
            print("No hay suficiente cantidad en el inventario.")

    # Método para actualizar la ubicación del producto en el inventario
    def actualizar_ubicacion(self, ubicacion):
        self.__ubicacion = ubicacion

    def eliminar_inventario(self, id_inventario):
        try:
            with open("Archivos/inventario.json", "r") as archivo:
                inventarios_data = json.load(archivo)
            
            indice = None
            for i, inventario_data in enumerate(inventarios_data):
                if inventario_data['id_inventario'] == id_inventario:
                    indice = i
                    break
            
            if indice is not None:
                del inventarios_data[indice]
                
                with open("Archivos/inventario.json", "w") as archivo:
                    json.dump(inventarios_data, archivo, indent=4)
                    
                print(f"Inventario con ID {id_inventario} eliminado correctamente.")
            else:
                print(f"No se encontró un inventario con ID {id_inventario}.")
                
        except FileNotFoundError:
            print("No se encontró el archivo inventario.json")
    
    # Método para guardar el inventario en un archivo JSON
    @staticmethod
    def guardar_inventario(nombre_archivo):
        inventarios_data = [{
            "id_inventario": inventario.get_id_inventario(),
            "producto_id": inventario.get_producto_id(),
            "cantidad": inventario.get_cantidad(),
            "ubicacion": inventario.get_ubicacion()
        } for inventario in Inventario.inventarios]
        with open(nombre_archivo, "w") as archivo:
            json.dump(inventarios_data, archivo, indent=4)
        print("Inventario guardado en el archivo:", nombre_archivo)

   
    def mostrar_inventario_por_id(id_inventario):
        id_inventario = str(id_inventario)
        try:
            with open("Archivos/inventario.json", "r") as archivo:
                inventarios_data = json.load(archivo)

            encontrado = False
            for inventario_data in inventarios_data:
                if inventario_data['id_inventario'] == str(id_inventario):
                    print("*****************")
                    print("Inventario encontrado:")
                    print(f"ID de Inventario: {inventario_data['id_inventario']}")
                    print(f"ID de Producto: {inventario_data['producto_id']}")
                    print(f"Cantidad: {inventario_data['cantidad']}")
                    print(f"Ubicación: {inventario_data['ubicacion']}")
                    encontrado = True
                    break

            if not encontrado:
                print(f"No se encontró un inventario con ID {id_inventario}.")

        except FileNotFoundError:
            print("No se encontró el archivo inventario.json")

    @staticmethod   
    def mostrar_todos_inventarios():
        try:
            with open("Archivos/inventario.json", "r") as archivo:
                inventarios_data = json.load(archivo)

            if inventarios_data:
                print("*****************")
                print("Inventarios encontrados:")
                for inventario_data in inventarios_data:
                    print("ID de Inventario:", inventario_data['id_inventario'])
                    print("ID de Producto:", inventario_data['producto_id'])
                    print("Cantidad:", inventario_data['cantidad'])
                    print("Ubicación:", inventario_data['ubicacion'])
                    print("------------------------------")
            else:
                print("No hay inventarios registrados.")

        except FileNotFoundError:
            print("No se encontró el archivo inventario.json")