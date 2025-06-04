# cliente.py 1.1
# Fecha: Mar, 2025
# @version: Gaelcyborg 1.1
# @autor: Douxvi

from cuenta import Cuenta # Importamos la clase Cuenta

class Cliente:
    """
    Clase que representa a un cliente del banco.
    Un cliente puede tener una cuenta bancaria asociada.
    """
    def __init__(self, nombre_completo: str, domicilio: str, anios_edad: int, cuenta_bancaria: Cuenta = None):
        """
        Se inicia un nuevo objeto Cliente.

        Defs:
            nombre_completo (str): Nombre completo del cliente.
            domicilio (str): Dirección del cliente.
            anios_edad (int): Edad del cliente.
            cuenta_bancaria (Cuenta, optional): Objeto Cuenta asociado al cliente.
        """
        self.__nombre = nombre_completo
        self.__direccion = domicilio
        self.__edad = anios_edad
        self.__cuenta_asociada = cuenta_bancaria # El cliente "tiene una" cuenta

    def asignar_cuenta(self, cuenta_bancaria: Cuenta):
        """
        Asigna o actualiza la cuenta bancaria del cliente.
        Defs:
            cuenta_bancaria (Cuenta): El objeto Cuenta a asociar.
        """
        self.__cuenta_asociada = cuenta_bancaria
        print(f"Cuenta asignada exitosamente al cliente {self.__nombre}.")

    def imprimir_detalles_cliente(self):
        """
        Muestra los detalles del cliente y su cuenta asociada en la consola.
        """
        print("\n--- Detalles del Cliente ---")
        print(f"Nombre: {self.__nombre}")
        print(f"Dirección: {self.__direccion}")
        print(f"Edad: {self.__edad} años")
        if self.__cuenta_asociada:
            print("--- Cuenta Bancaria Asociada ---")
            self.__cuenta_asociada.imprimir_detalles_cuenta()
        else:
            print("El cliente no tiene una cuenta bancaria asignada actualmente.")

    # Getters (opcional, pero por si se necesitan desde fuera)
    def get_nombre(self) -> str:
        return self.__nombre

    def get_cuenta_asociada(self) -> Cuenta:
        return self.__cuenta_asociada
