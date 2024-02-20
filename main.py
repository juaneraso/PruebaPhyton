

""" Clase inventario """
import json

from cliente import Cliente
from producto import Producto
from venta import Venta
from inventario import Inventario
from configuracion import Configuracion
from producto import Producto


controlador1 = 0

while controlador1 != 6:

  print("************** MENU DE OPCIONES ****")
  print("1. Ventas")
  print("2. Clientes")
  print("3. Productos")
  print("4. Inventarios")
  print("5. Configuraciones")
  print("6. Cerrar Sesion")
  print("******************")

  controlador1 = int(input("Ingrese una opcion: "))
  if controlador1 == 1:
    print("1. Registrar Venta")
    print("2. Historial de Ventas")
    print("3. Eliminar una venta")
    print("4. Buscar una venta")
    opcion_venta = int(input("Ingrese una opicion de venta:"))  

    if opcion_venta == 1:
      id_cliente = input("Ingrese el ID del cliente: ")
      nombre_cliente = input("Ingrese el nombre del cliente: ")
      direccion_cliente = input("Ingrese la dirección del cliente: ")
      telefono_cliente = input("Ingrese el teléfono del cliente: ")

      # Crear una instancia de Cliente con los datos ingresados por el usuario
      cliente = Cliente(id_cliente, nombre_cliente, direccion_cliente, telefono_cliente)

      # Solicitar los datos de la venta al usuario
      id_venta = int(input("Ingrese el ID de la venta: "))
      monto_venta = float(input("Ingrese el monto de la venta: "))    
      # Crear una instancia de Venta con el cliente creado
      venta = Venta(id_venta, monto_venta, cliente)

      # Guardar la venta en el archivo de ventas
      venta.guardar_venta()
    elif opcion_venta == 2:
      Venta.mostrar_ventas()
    elif opcion_venta == 3:
      id_venta2 = int(input("Ingrese el ID de la venta: "))
      Venta.eliminar_venta(id_venta2)
    elif opcion_venta == 4:      
      id_cliente = int(input("Ingrese el ID del cliente: "))
      Venta.buscar_venta_por_id_cliente(id_cliente)
   

  elif controlador1 == 2:
    print("\nMenú de Cliente:")
    print("1. Registrar un nuevo cliente")
    print("2. Eliminar un cliente")
    print("3. Buscar un cliente por ID")
    print("4. Actualizar los datos de un cliente")
    print("5. Ver la lista de clientes")
    print("6. Salir")


    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        id_cliente = input("Ingrese el ID del cliente: ")
        nombre = input("Ingrese el nombre del cliente: ")
        direccion = input("Ingrese la dirección del cliente: ")
        telefono = input("Ingrese el teléfono del cliente: ")
        Cliente.registrar_cliente(id_cliente, nombre, direccion, telefono)

    elif opcion == "2":
        id_cliente = input("Ingrese el ID del cliente a eliminar: ")
        Cliente.eliminar_cliente(id_cliente)

    elif opcion == "3":
        id_cliente = input("Ingrese el ID del cliente a buscar: ")
        cliente = Cliente.buscar_cliente(id_cliente)
        if cliente:
            print("Información del cliente:")
            print(cliente)

    elif opcion == "4":
        id_cliente = input("Ingrese el ID del cliente a actualizar: ")
        nombre = input("Ingrese el nuevo nombre del cliente (deje en blanco para no actualizar): ")
        direccion = input("Ingrese la nueva dirección del cliente (deje en blanco para no actualizar): ")
        telefono = input("Ingrese el nuevo teléfono del cliente (deje en blanco para no actualizar): ")
        Cliente.actualizar_cliente(id_cliente, nombre, direccion, telefono)

    elif opcion == "5":
        Cliente.ver_lista_clientes()


  elif controlador1 == 3:
        print("\nMENU:")
        print("1. Crear Producto")
        print("2. Eliminar Producto")
        print("3. Ver Productos")
        print("4. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            # Solicitar los datos del producto al usuario
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            descripcion = input("Ingrese la descripción del producto: ")
            precio = float(input("Ingrese el precio del producto: "))

            producto = Producto(id_producto, nombre, descripcion, precio)
            # Guardar el producto en el archivo JSON
            producto.guardar_producto()

        elif opcion == "2":
            # Solicitar el ID del producto que se desea eliminar
            id_producto_a_eliminar = input("Ingrese el ID del producto que desea eliminar: ")

            # Eliminar el producto
            Producto.eliminar_producto(id_producto_a_eliminar)

        elif opcion == "3":
            # Ver todos los productos
            Producto.ver_productos()
    
    
  elif controlador1 == 4:
      print("1. Crear Inventario")
      print("2. Eliminar Inventario")
      print("3. Ver Inventario")
      print("4. Ver todos los inventarios")

      opcion_inventario = int(input("Seleccione una opción: "))

      if opcion_inventario == 1:
          nombre_archivo = "Archivos/inventario.json"
          id_inventario = input("Ingrese el ID del inventario: ")
          producto_id = input("Ingrese el ID del producto: ")
          cantidad = input("Ingrese la cantidad del producto: ")
          ubicacion = input("Ingrese la ubicación del producto: ")

          inventario = Inventario(id_inventario, producto_id, cantidad, ubicacion)
          inventario.guardar_inventario(nombre_archivo)
          print("Inventario creado y guardado exitosamente.")
      elif opcion_inventario == 2:
          id_inventario_a_eliminar = input("Ingrese el ID del inventario a eliminar: ")
          inventario = Inventario("Archivos/inventario.json")  # Crear un objeto Inventario
          inventario.eliminar_inventario(id_inventario_a_eliminar)
      elif opcion_inventario == 3:
  
          id_inventario = input("Ingrese el ID del inventario:")
          Inventario.mostrar_inventario_por_id(id_inventario)
      elif opcion_inventario == 4:
          Inventario.mostrar_todos_inventarios()
      else:
          print("Opción no válida.")


  elif controlador1 == 5:
    print("Configuracion")
    print("1. Iniciar Sesion")
    print("2. Agregar Usuarios")
    print("3. Restrablecer Contraseñas")
    print("4. Ver Usuarios Registrados")

    configuracion = Configuracion()
    opcion_configuracion = int(input("Ingrese una opción de configuración: "))
    print("******************")
    if opcion_configuracion == 1:
              usuario = input("Ingrese su nombre de usuario: ")
              contrasena = input("Ingrese su contraseña: ")
              configuracion.iniciar_sesion(usuario, contrasena)
    elif opcion_configuracion == 2:
              usuario = input("Ingrese el nombre del nuevo usuario: ")
              contrasena = input("Ingrese la contraseña del nuevo usuario: ")
              configuracion.registrar_usuario(usuario, contrasena)
    elif opcion_configuracion == 3:
              usuario = input("Ingrese el nombre del usuario para restablecer su contraseña: ")
              nueva_contrasena = input("Ingrese la nueva contraseña: ")
              configuracion.restablecer_contrasena(usuario, nueva_contrasena)
    elif opcion_configuracion == 4:
              configuracion.ver_usuarios_registrados()
    else:
              print("Opción no válida.")
      

    #Diseñe un algoritmo encriptador de contraseñas
    # a = 4
    # e = 3
    # i = 1
    # o = 0
    # ñ = #

    # Input
    # Estaesmicontraseña

    # Output
    # est43sm1c0ntr4s3#4

    # El sistema debe guardar la contraseña encriptada en un archivo llamado contraseñas.txt
    # Al iniciar sesion con la contraseña se debe usar el agoritmo de encriptacion para comparase con la contraseña almacenada.
    # El sistema debe permitir restablecer la contraseña de un usuario
    # El sistema debe permitir ver la lisa de los usuarios creados

