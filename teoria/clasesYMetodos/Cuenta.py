# cuenta.py
# Fecha: Feb, 2025
# @version: Cyborgael 1.0
# @autor: Douxvi

class Cuenta:
    """
    Clase que representa una cuenta bancaria.
    """
    def __init__(self, saldo_inicial: float, tipo_de_cuenta: str, nombre_propietario: str):
        """
        Nueva cuenta bancaria.

        Defs:
            saldo_inicial (float): El saldo con el que se abre la cuenta.
            tipo_de_cuenta (str): El tipo de cuenta (ej. "ahorros", "corriente").
            nombre_propietario (str): Nombre del titular de la cuenta.
        """
        if saldo_inicial < 0:
            print("Advertencia: El saldo inicial no puede ser negativo. Se establecerá en 0.")
            self.__saldo_actual = 0.0
        else:
            self.__saldo_actual = float(saldo_inicial)
        self.__tipo_cuenta = tipo_de_cuenta
        self.__propietario = nombre_propietario 

    def imprimir_detalles_cuenta(self):
        """
        Muestra los detalles de la cuenta en la consola.
        """
        print("\n--- Detalles de la Cuenta ---")
        print(f"Propietario: {self.__propietario}")
        print(f"Tipo de Cuenta: {self.__tipo_cuenta}")
        print(f"Saldo Disponible: ${self.__saldo_actual:.2f}")

    def depositar_monto(self, monto: float):
        """
        Deposita un monto en la cuenta.

        Defs:
            monto (float): La cantidad a depositar. Debe ser positiva.
        """
        if monto <= 0:
            print("Error: El monto a depositar debe ser positivo.")
        else:
            self.__saldo_actual += monto
            print(f"Depósito de ${monto:.2f} realizado. Nuevo saldo: ${self.__saldo_actual:.2f}")

    def retirar_monto(self, monto: float):
        """
        Retira un monto de la cuenta.

        Defs:
            monto (float): La cantidad a retirar. Debe ser positiva y no exceder el saldo.
        """
        if monto <= 0:
            print("Error: El monto a retirar debe ser positivo.")
        elif monto > self.__saldo_actual:
            print("Error: Fondos insuficientes para realizar el retiro.")
        else:
            self.__saldo_actual -= monto
            print(f"Retiro de ${monto:.2f} realizado. Nuevo saldo: ${self.__saldo_actual:.2f}")
