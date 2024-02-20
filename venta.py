import json
from cliente import Cliente

class Venta:
    @staticmethod
    def cargar_ventas():
        try:
            with open("Archivos/ventas.json", "r") as archivo:
                ventas_data = json.load(archivo)
                ventas = []
                for venta_data in ventas_data:
                    id_venta = venta_data['id_venta']
                    monto_venta = venta_data['monto_venta']
                    cliente_data = venta_data['cliente']
                    if cliente_data:
                        cliente = Cliente(cliente_data['id_cliente'], cliente_data['nombre_cliente'], cliente_data['direccion_cliente'], cliente_data['telefono_cliente'])
                    else:
                        cliente = None
                    venta = Venta(id_venta, monto_venta, cliente)
                    ventas.append(venta)
                return ventas
        except FileNotFoundError:
            print("No se encontró el archivo ventas.json. No hay ventas registradas.")
            return []

    @staticmethod
    def mostrar_ventas():
        ventas = Venta.cargar_ventas()
        if ventas:
            print("Ventas registradas:")
            for venta in ventas:
                print(venta)
        else:
            print("No hay ventas registradas.")

    def guardar_venta(self):
        ventas = self.cargar_ventas()
        ventas.append(self)
        ventas_data = [venta.to_dict() for venta in ventas]
        with open("Archivos/ventas.json", "w") as archivo:
            json.dump(ventas_data, archivo, indent=4)

    def __init__(self, id_venta, monto_venta, cliente):
        self.__id_venta = id_venta
        self.__monto_venta = monto_venta
        self.__cliente = cliente

    # Métodos para establecer y obtener los atributos de la venta
    def set_id_venta(self, id_venta):
        self.__id_venta = id_venta

    def get_id_venta(self):
        return self.__id_venta

    def set_monto_venta(self, monto_venta):
        self.__monto_venta = monto_venta

    def get_monto_venta(self):
        return self.__monto_venta

    def set_cliente(self, cliente):
        self.__cliente = cliente

    def get_cliente(self):
        return self.__cliente

    # Método para imprimir la información de la venta
    def __str__(self):
        if self.__cliente:
            return f"ID de Venta: {self.__id_venta}, Monto: {self.__monto_venta}, Cliente asociado: {self.__cliente.get_nombre_cliente()}"
        else:
            return f"ID de Venta: {self.__id_venta}, Monto: {self.__monto_venta}, No hay cliente asociado a la venta"

    # Método para convertir la venta a un diccionario
    def to_dict(self):
        venta_dict = {
            "id_venta": self.__id_venta,
            "monto_venta": self.__monto_venta,
            "cliente": {
                "id_cliente": self.__cliente.get_id_cliente(),
                "nombre_cliente": self.__cliente.get_nombre(),
                "direccion_cliente": self.__cliente.get_direccion(),
                "telefono_cliente": self.__cliente.get_telefono()
            } if self.__cliente else None
        }
        return venta_dict
    
    @staticmethod
    def eliminar_venta(id_venta):
        ventas = Venta.cargar_ventas()
        ventas_actualizadas = [venta for venta in ventas if venta.get_id_venta() != id_venta]
        if len(ventas) == len(ventas_actualizadas):
            print("No se encontró ninguna venta con ese ID.")
        else:
            ventas_data = [venta.to_dict() for venta in ventas_actualizadas]
            with open("Archivos/ventas.json", "w") as archivo:
                json.dump(ventas_data, archivo, indent=4)
            print("Venta eliminada correctamente.")

    @staticmethod
    def buscar_venta_por_id_cliente(id_cliente):
        ventas = Venta.cargar_ventas()
        ventas_encontradas = [venta for venta in ventas if venta.get_cliente().get_id_cliente() == str(id_cliente)]
        if ventas_encontradas:
            print("Ventas encontradas para el cliente:")
            for venta in ventas_encontradas:
                print(venta)
        else:
            print("No se encontraron ventas para el cliente con el ID especificado.")


    def __str__(self):
        if self.__cliente:
            return f"ID de Venta: {self.__id_venta}, Monto: {self.__monto_venta}, Cliente asociado: {self.__cliente.get_nombre()}"
        else:
            return f"ID de Venta: {self.__id_venta}, Monto: {self.__monto_venta}, No hay cliente asociado a la venta"
