# cliente.py
# Fecha: Feb, 2025
# @version: Gaelcyborg 1.0
# @autor: Douxvi

class Cliente:
    """
    Clase que representa a un cliente del banco.
    """
    def __init__(self, nombre_completo: str, domicilio: str, anios_edad: int):
        """
        Nuevo objeto Cliente.

        Defs:
            nombre_completo (str): Nombre completo del cliente.
            domicilio (str): Dirección del cliente.
            anios_edad (int): Edad del cliente.
        """
        self.__nombre = nombre_completo
        self.__direccion = domicilio
        self.__edad = anios_edad
      

    def imprimir_detalles_cliente(self):
        """
        Muestra los detalles del cliente en la consola.
        """
        print("\n--- Detalles del Cliente ---")
        print(f"Nombre: {self.__nombre}")
        print(f"Dirección: {self.__direccion}")
        print(f"Edad: {self.__edad} años")
