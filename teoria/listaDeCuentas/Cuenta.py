# cuenta.py 3.0
# Fecha: abr, 2025
# @version: Cyborgael 1.2
# @autor: Douxvi

class Cuenta:
    """
    Clase que representa una cuenta bancaria.
    Ahora incluye tipOs de cuenta predefinidos y un método __str__.
    """
    # Tipos de cuenta válidos, como en listaDeCuentas/Cuenta.py
    TIPOS_DE_CUENTA_VALIDOS = ['credito', 'debito', 'nomina'] #

    def __init__(self, saldo_inicial: float, tipo_de_cuenta: str): 
        """
        Inicializa una nueva cuenta bancaria.

        Defs:
            saldo_inicial (float): El saldo con el que se abre la cuenta.
            tipo_de_cuenta (str): El tipo de cuenta. Debe ser uno de TIPOS_DE_CUENTA_VALIDOS.

        !!!:
            ValueError: Si el tipo_de_cuenta no es válido.
        """
        if tipo_de_cuenta.lower() not in self.TIPOS_DE_CUENTA_VALIDOS: #
            raise ValueError(
                f"Tipo de cuenta '{tipo_de_cuenta}' no válido. "
                f"Debe ser uno de: {', '.join(self.TIPOS_DE_CUENTA_VALIDOS)}"
            )
        self.__tipo_cuenta = tipo_de_cuenta.lower()

        if saldo_inicial < 0:
            print(f"Advertencia para cuenta tipo '{self.__tipo_cuenta}': "
                  "El saldo inicial no puede ser negativo. Se establecerá en 0.")
            self.__saldo_actual = 0.0
        else:
            self.__saldo_actual = float(saldo_inicial)

    def imprimir_detalles_cuenta(self):
        """
        Muestra los detalles de la cuenta en la consola.
        (Usaremos __str__ para la representación principal ahora)
        """
        print(str(self))

    def depositar_monto(self, monto: float):
        """
        Deposita un monto en la cuenta.

        Defs:
            monto (float): La cantidad a depositar. Debe ser positiva.
        Devuelve:
            str: Mensaje indicando el resultado de la operación.
        """
        if monto <= 0:
            return "Error: El monto a depositar debe ser positivo." #
        else:
            self.__saldo_actual += monto
            return f"Depósito de ${monto:.2f} realizado. Nuevo saldo: ${self.__saldo_actual:.2f}" #

    def retirar_monto(self, monto: float):
        """
        Retira un monto de la cuenta.

        Defs:
            monto (float): La cantidad a retirar. Debe ser positiva y no exceder el saldo.
        Devuelve:
            str: Mensaje indicando el resultado de la operación.
        """
        if monto <= 0:
            return "Error: La cantidad a retirar no puede ser negativa." #
        elif monto > self.__saldo_actual:
            return "Error: Fondos insuficientes para realizar el retiro." #
        else:
            self.__saldo_actual -= monto
            return f"Retiro de ${monto:.2f} realizado. Nuevo saldo: ${self.__saldo_actual:.2f}" #

    def get_saldo(self) -> float:
        return self.__saldo_actual

    def set_saldo(self, nuevo_saldo: float): #
        if nuevo_saldo >= 0:
            self.__saldo_actual = nuevo_saldo
        else:
            print("Error: El saldo no puede ser negativo.")

    def get_tipo(self) -> str:
        return self.__tipo_cuenta

    def __str__(self) -> str:
        """
        Devuelve una representación en cadena de la cuenta
        """
        return (f"Tipo de Cuenta: {self.__tipo_cuenta.capitalize()} | "
                f"Saldo Disponible: ${self.__saldo_actual:.2f}")
