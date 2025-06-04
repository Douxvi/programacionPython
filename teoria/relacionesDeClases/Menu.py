# menu.py 2.0
# Fecha: Mar, 2025
# @version: Cyborgael 1.1
# @autor: Douxvi
from cuenta import Cuenta # Necesario si el menú opera directamente sobre una cuenta

class Menu:
    """
    Clase que gestiona el menú interactivo del sistema bancario.
    """
    def __init__(self, saludo_inicial: str, cuenta_operable: Cuenta = None):
        """
        Inicializa el menú.

        defs:
            saludo_inicial (str): El mensaje de bienvenida para el usuario.
            cuenta_operable (Cuenta, optional): La cuenta sobre la que operará el menú.
                                            
        """
        self.__saludo = saludo_inicial
        self.__cuenta_actual = cuenta_operable 

    def dar_saludos(self): 
        """
        Muestra el mensaje de bienvenida configurado.
        """
        print(f"\n*** {self.__saludo} ***")
        if self.__cuenta_actual:
            print(f"Operando con la cuenta de: {self.__cuenta_actual._Cuenta__propietario_cuenta}") # Acceso al nombre del propietario
        else:
            print("Advertencia: No hay una cuenta seleccionada para operar.")

    def opcion_retirar(self): # Equivalente a OpcionRetirar
        """
        Gestiona la opción de retirar dinero. Por ahora solo imprime un mensaje.
        """
        print("-> Está en la opción de Retirar dinero.")
        if self.__cuenta_actual:
            # Aquí iría la lógica para solicitar monto y llamar a self.__cuenta_actual.retirar_monto(cantidad)
            # Por ahora, solo mensaje:
            # cantidad = float(input('Cantidad que desea retirar: '))
            # self.__cuenta_actual.retirar_monto(cantidad)
            # print(f"Saldo después del retiro: {self.__cuenta_actual.get_saldo()}") (nota 1)
            pass
        else:
            print("No hay cuenta activa para realizar un retiro.")


    def opcion_depositar(self): # Equivalente a OpcionDepositar
        """
        Gestiona la opción de depositar dinero. Por ahora solo imprime un mensaje.
        """
        print("-> Está en la opción de Depositar dinero.")
        if self.__cuenta_actual:
          #Lo mismo que (nota) 
            pass
        else:
            print("No hay cuenta activa para realizar un depósito.")

    def opcion_salir(self): # Equivalente a OpcionSalir
        """
        Gestiona la opción de salir del menú.
        """
        print("-> Ha seleccionado Salir. ¡Gracias por usar nuestros servicios!")

    def desplegar_opciones_principales(self): # Equivalente a desplegarOpciones
        """
        Muestra el menú de opciones principales y procesa la selección del usuario.
        """
        if not self.__cuenta_actual:
            print("No se pueden desplegar opciones sin una cuenta activa.")
            return

        while True:
            print("\nSeleccione una opción para la cuenta de "
                  f"{self.__cuenta_actual._Cuenta__propietario_cuenta}:")
            print("1. Retirar")
            print("2. Depositar")
            print("3. Salir")

            opcion_elegida = input("Ingrese el número de la opción deseada: ")

            if opcion_elegida == '1':
                self.opcion_retirar()
            elif opcion_elegida == '2':
                self.opcion_depositar()
            elif opcion_elegida == '3':
                self.opcion_salir()
                break  # Sale del bucle while
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
