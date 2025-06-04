# cliente.py 3.0
# Fecha: Abr, 2025
# @version: Cyborgael 1.2 
# @autor: Douxvi

from typing import List
from cuenta import Cuenta

class Cliente:
    """
    Clase que representa a un cliente del banco.
    Un cliente ahora puede tener múltiples cuentas bancarias.
    """
    def __init__(self, nombre_completo: str, domicilio: str, anios_edad: int, cuentas_iniciales: Optional[List[Cuenta]] = None):
        """
        Inicia un nuevo objeto Cliente.

        Defs:
            nombre_completo (str): Nombre completo del cliente.
            domicilio (str): Dirección del cliente.
            anios_edad (int): Edad del cliente.
            cuentas_iniciales (Optional[List[Cuenta]], optional): Lista inicial de cuentas. Defaults to None.
        """
        self.__nombre = nombre_completo
        self.__direccion = domicilio
        self.__edad = anios_edad
        self.__lista_cuentas: List[Cuenta] = [] 
        if cuentas_iniciales:
            for cta in cuentas_iniciales:
                if isinstance(cta, Cuenta):
                    self.__lista_cuentas.append(cta)
                else:
                    print(f"Advertencia: El objeto {cta} no es una instancia válida de Cuenta y no será agregado.")


    def agregar_cuenta(self, nueva_cuenta: Cuenta): #
        """
        Agrega una nueva cuenta a la lista de cuentas del cliente.

        Defs:
            nueva_cuenta (Cuenta): El objeto Cuenta a agregar.
        """
        if isinstance(nueva_cuenta, Cuenta):
            self.__lista_cuentas.append(nueva_cuenta)
            print(f"Cuenta tipo '{nueva_cuenta.get_tipo()}' agregada exitosamente al cliente {self.__nombre}.")
        else:
            # Se podría lanzar un TypeError
            # raise TypeError("El objeto no es una instancia de la clase Cuenta.")
            print("Error: El objeto proporcionado no es una instancia válida de Cuenta.")


    def eliminar_cuenta(self, indice: int): #
        """
        Elimina una cuenta de la lista del cliente por su índice.

        Defs:
            indice (int): El índice de la cuenta a eliminar.
        """
        try:
            cuenta_eliminada = self.__lista_cuentas.pop(indice)
            print(f"Cuenta '{str(cuenta_eliminada)}' eliminada exitosamente para el cliente {self.__nombre}.")
        except IndexError:
            print(f"Error: Índice {indice} inválido. No se pudo eliminar la cuenta.")
        except Exception as e:
            print(f"Error inesperado al eliminar cuenta: {e}")

    def info_cuentas(self): #
        """
        Muestra información detallada de todas las cuentas del cliente.
        """
        print(f"\n--- Cuentas de: {self.__nombre} ---")
        if not self.__lista_cuentas:
            print("Este cliente no tiene cuentas bancarias registradas.")
            return
        for i, cuenta_obj in enumerate(self.__lista_cuentas):
            print(f"Índice [{i}]: {str(cuenta_obj)}")

    def imprimir_detalles_cliente(self): # Modificao para reflejar múltiples cuentas
        """
        Muestra los detalles del cliente y un resumen de sus cuentas.
        """
        print(str(self))


    # Getters
    def get_nombre(self) -> str: #
        return self.__nombre

    def get_direccion(self) -> str: #
        return self.__direccion

    def get_edad(self) -> int: #
        return self.__edad

    def get_lista_cuentas(self) -> List[Cuenta]: #
        return self.__lista_cuentas

    def __str__(self) -> str: #
        """
        Devuelve una representación en cadena del cliente y sus cuentas.
        """
        detalles_cliente = (
            f"--- Detalles del Cliente ---\n"
            f"Nombre: {self.__nombre}\n"
            f"Dirección: {self.__direccion}\n"
            f"Edad: {self.__edad} años\n"
            f"--- Cuentas Registradas ---"
        )
        if not self.__lista_cuentas:
            cuentas_str = "El cliente no tiene cuentas bancarias asignadas."
        else:
            # une los __str__ de cada cuenta
            cuentas_str = "\n".join([f"  Índice [{i}]: {str(cta)}" for i, cta in enumerate(self.__lista_cuentas)]) #
        return f"{detalles_cliente}\n{cuentas_str}"
