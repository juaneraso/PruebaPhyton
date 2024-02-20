

import json

class Producto:
    def __init__(self, id_producto, nombre, descripcion, precio):
        self.__id_producto = str(id_producto)
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio = precio

    def set_id_producto(self, id_producto):
        self.__id_producto = str(id_producto)

    def get_id_producto(self):
        return self.__id_producto

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    def get_descripcion(self):
        return self.__descripcion

    def set_precio(self, precio):
        self.__precio = precio

    def get_precio(self):
        return self.__precio

    def guardar_producto(self):
        productos = Producto.cargar_productos()
        productos.append(self)
        productos_data = [producto.to_dict() for producto in productos]
        with open("Archivos/productos.json", "w") as archivo:
            json.dump(productos_data, archivo, indent=4)
    @staticmethod
    def eliminar_producto(id_producto_a_eliminar):
        productos = Producto.cargar_productos()
        indice = None
        for i, producto in enumerate(productos):
            if producto.get_id_producto() == id_producto_a_eliminar:
                indice = i
                break

        if indice is not None and indice < len(productos):
            del productos[indice]
            productos_data = [producto.to_dict() for producto in productos]
            with open("Archivos/productos.json", "w") as archivo:
                json.dump(productos_data, archivo, indent=4)
            print("Producto eliminado correctamente.")
        else:
            print("El producto no existe en la lista.")



    @staticmethod
    def ver_productos():
        try:
            with open("Archivos/productos.json", "r") as archivo:
                productos_data = json.load(archivo)
                print("Lista de productos:")
                for producto_data in productos_data:
                    id_producto = producto_data['id_producto']
                    nombre = producto_data['nombre']
                    descripcion = producto_data['descripcion']
                    precio = producto_data['precio']
                    print(f"ID: {id_producto}, Nombre: {nombre}, Descripción: {descripcion}, Precio: {precio}")
        except FileNotFoundError:
            print("No se encontró el archivo productos.json. No hay productos registrados.")

    @staticmethod
    def cargar_productos():
        try:
            with open("Archivos/productos.json", "r") as archivo:
                productos_data = json.load(archivo)
                productos = []
                for producto_data in productos_data:
                    id_producto = producto_data['id_producto']
                    nombre = producto_data['nombre']
                    descripcion = producto_data['descripcion']
                    precio = producto_data['precio']
                    producto = Producto(id_producto, nombre, descripcion, precio)
                    productos.append(producto)
                return productos
        except FileNotFoundError:
            print("No se encontró el archivo productos.json. No hay productos registrados.")
            return []

    def to_dict(self):
        return {
            "id_producto": self.__id_producto,
            "nombre": self.__nombre,
            "descripcion": self.__descripcion,
            "precio": self.__precio
        }
