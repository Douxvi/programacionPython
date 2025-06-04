# menu.py 3.0
# Fecha: Abr, 2025
# @version: Cyborgael 1.2
# @autor: Douxvi

from cliente import Cliente # El menú ahora interactúa con un Cliente
from cuenta import Cuenta

class Menu:
    """
    Clase que gestiona el menú interactivo del sistema bancario.
    Ahora adaptado para clientes con múltiples cuentas.
    """
    def __init__(self, saludo_inicial: str, cliente_actual: Cliente):
        """
        Inicia el menú.

        Defs:
            saludo_inicial (str): El mensaje de bienvenida para el usuario.
            cliente_actual (Cliente): El cliente que está utilizando el menú.
        """
        self.__saludo = saludo_inicial
        self.__cliente_actual = cliente_actual
        self.__cuenta_seleccionada: Optional[Cuenta] = None # La cuenta específica para operar

    def dar_saludos(self):
        """
        Muestra el mensaje de bienvenida configurado.
        """
        print(f"\n*** {self.__saludo}, {self.__cliente_actual.get_nombre()}! ***")

    def seleccionar_cuenta_operable(self) -> bool:
        """
        Permite al cliente seleccionar una de sus cuentas para realizar operaciones.

        Devuelve:
            bool: True si se seleccionó una cuenta, False si no o si el cliente no tiene cuentas.
        """
        self.__cliente_actual.info_cuentas() # Muestra las cuentas disponibles
        lista_de_cuentas_cliente = self.__cliente_actual.get_lista_cuentas()

        if not lista_de_cuentas_cliente:
            print("No tiene cuentas registradas para seleccionar.")
            return False

        while True:
            try:
                indice_str = input(f"Ingrese el índice de la cuenta con la que desea operar (0-{len(lista_de_cuentas_cliente)-1}), o 's' para salir: ")
                if indice_str.lower() == 's':
                    self.__cuenta_seleccionada = None
                    return False
                indice_seleccionado = int(indice_str)
                if 0 <= indice_seleccionado < len(lista_de_cuentas_cliente):
                    self.__cuenta_seleccionada = lista_de_cuentas_cliente[indice_seleccionado]
                    print(f"Ha seleccionado la cuenta: {str(self.__cuenta_seleccionada)}")
                    return True
                else:
                    print("Índice fuera de rango. Intente nuevamente.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número de índice o 's'.")


    def opcion_retirar(self): # Funcionalidad completa ¡ESTAAA VIVOOO!
        """
        Gestiona la opción de retirar dinero de la cuenta seleccionada.
        """
        if not self.__cuenta_seleccionada:
            print("Error: No hay una cuenta seleccionada para retirar.")
            return

        print(f"-> Operación Retirar en cuenta: {str(self.__cuenta_seleccionada)}")
        try:
            cantidad_str = input("Ingrese la cantidad que desea retirar: ")
            cantidad = float(cantidad_str)
            if cantidad < 0: # Adicional al chequeo en Cuenta, para un feedback inmediato.
                 print("Error: La cantidad a retirar no puede ser negativa.") #
                 return
            mensaje_operacion = self.__cuenta_seleccionada.retirar_monto(cantidad)
            print(mensaje_operacion)
            # print(f"Saldo después del retiro: {self.__cuenta_seleccionada.get_saldo()}") # El mensaje ya lo incluye
        except ValueError:
            print("Error: Cantidad no válida. Debe ingresar un número.")
        except Exception as e:
            print(f"Error inesperado durante el retiro: {e}")


    def opcion_depositar(self): # Funcionalidad completa ¡YA TOMÓ FORMA!
        """
        Gestiona la opción de depositar dinero en la cuenta seleccionada.
        """
        if not self.__cuenta_seleccionada:
            print("Error: No hay una cuenta seleccionada para depositar.")
            return

        print(f"-> Operación Depositar en cuenta: {str(self.__cuenta_seleccionada)}")
        try:
            cantidad_str = input("Ingrese la cantidad que desea depositar: ")
            cantidad = float(cantidad_str)
            if cantidad < 0: # También adicional al chequeo en Cuenta
                 print("Error: La cantidad a depositar no puede ser negativa.")
                 return
            mensaje_operacion = self.__cuenta_seleccionada.depositar_monto(cantidad)
            print(mensaje_operacion)
            # print(f"Saldo después del depósito: {self.__cuenta_seleccionada.get_saldo()}") # El mensaje ya lo incluye
        except ValueError:
            print("Error: Cantidad no válida. Debe ingresar un número.")
        except Exception as e:
            print(f"Error inesperado durante el depósito: {e}")


    def opcion_salir(self):
        """
        Gestiona la opción de salir del menú de operaciones de cuenta.
        """
        print("-> Ha seleccionado Salir de las operaciones de esta cuenta.")
        self.__cuenta_seleccionada = None # Deseleccionar cuenta al salir de sus operaciones


    def desplegar_menu_principal_cliente(self):
        """
        Menú principal para un cliente: seleccionar cuenta o salir del sistema.
        """
        self.dar_saludos()
        while True:
            print("\n--- Menú Cliente ---")
            print("1. Seleccionar cuenta para operar")
            print("2. Ver información de mis cuentas")
            print("3. Salir del sistema")
            opcion_menu_cliente = input("Seleccione una opción: ")

            if opcion_menu_cliente == '1':
                if self.seleccionar_cuenta_operable(): # Si se seleccionó una sola cuenta
                    self.desplegar_opciones_de_cuenta_actual() # Mostrar menú de operaciones para esa cuenta
                # Si no se seleccionó cuenta (ej. el cliente escribió 's' o no tiene cuentas), vuelve al menú cliente.
            elif opcion_menu_cliente == '2':
                self.__cliente_actual.info_cuentas()
            elif opcion_menu_cliente == '3':
                print("¡Gracias por utilizar el Banco Digital City Cyborg! Hasta pronto.")
                break
            else:
                print("Opción no válida. Intente nuevamente.")


    def desplegar_opciones_de_cuenta_actual(self):
        """
        Muestra el menú de operaciones para la cuenta actualmente seleccionada y procesa la selección.
        """
        if not self.__cuenta_seleccionada: # Doble chequeo, aunque seleccionar_cuenta_operable debería manejarlo.
            print("No hay cuenta seleccionada para operar. Regresando al menú anterior.")
            return

        print(f"\n--- Operaciones para la cuenta: {str(self.__cuenta_seleccionada)} ---")
        while self.__cuenta_seleccionada: # Continuar mientras haya una cuenta seleccionada
            print("\nSeleccione una operación:")
            print("1. Retirar")
            print("2. Depositar")
            print("3. Volver al menú de selección de cuenta") # Cambiado de "Salir" a ser más específico

            opcion_elegida = input("Ingrese el número de la opción deseada: ")

            if opcion_elegida == '1':
                self.opcion_retirar()
            elif opcion_elegida == '2':
                self.opcion_depositar()
            elif opcion_elegida == '3':
                self.opcion_salir() # Esto pondrá self.__cuenta_seleccionada a None y romperá el bucle
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
