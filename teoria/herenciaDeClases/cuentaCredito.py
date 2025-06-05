# cuentaCredito.py (Cuenta hija)
# Fecha: May, 2025
# @version: Cyborgaelini 1.3 
# @autor: Douxvi

from cuenta import Cuenta

class CuentaCredito(Cuenta):
    """
    Representa una cuenta de crédito, que es hija de Cuenta (Por herencia).
    Permite un saldo negativo hasta un límite de crédito.
    """
    def __init__(self, saldo_inicial: float, propietario: str, limite_credito: float):
        """
        Inicia una cuenta de crédito.

        Defs:
            saldo_inicial (float): Saldo inicial. Puede ser 0 o positivo (si hay sobrepago).
                                   Representa el balance actual.
            propietario (str): Nombre del propietario.
            limite_credito (float): Límite máximo de crédito (cuánto puede llegar a deber).
                                   Debe ser un valor positivo.
        """
        super().__init__(saldo_inicial, propietario)
        self.__tipo_cuenta = "Credito" # Atributo específico
        if limite_credito < 0:
            # Justificación: El límite de crédito debe ser un valor positivo o cero.
            print(f"Advertencia (Crédito - {propietario}): Límite de crédito no puede ser negativo. Se ajustará a 0.")
            self._limite_credito = 0.0
        else:
            # Atributo que justifica el diseño de CuentaCredito: Límite de crédito
            self._limite_credito = limite_credito

    def retirar_monto(self, monto: float) -> str:
        """
        Se sobrescribe el método para retirar dinero (realizar un gasto).
        Permite que el saldo se vuelva negativo hasta el límite de crédito.

        Justificación de la Sobrescritura:
        Las cuentas de crédito permiten gastar ("retirar") fondos que no tienes jaja
        directamente como saldo positivo, acumulando deuda hasta un límite establecido.
        El saldo representa el balance (positivo si se pagó de más, negativo si se debe).
        """
        if monto <= 0:
            return "Error: El monto del gasto debe ser positivo."

        # Justificación de diseño: Puede sobregirar hasta el límite de crédito.
        # El nuevo saldo después del retiro sería self._saldo_actual - monto.
        # Este nuevo saldo no debe ser menor que -self._limite_credito.
        # (saldo - monto) >= -limite  =>  saldo + limite >= monto
        if (self._saldo_actual - monto) < -self._limite_credito:
            disponible_real = self._saldo_actual + self._limite_credito
            return (f"Error: Gasto excede el límite de crédito. "
                    f"Límite de crédito: ${self._limite_credito:.2f}. "
                    f"Saldo actual: ${self._saldo_actual:.2f}. "
                    f"Disponible para gastar: ${disponible_real if disponible_real > 0 else 0:.2f}.")

        self._saldo_actual -= monto # El saldo disminuye (puede volverse más negativo)
        return (f"Gasto con crédito de ${monto:.2f} realizado. "
                f"Nuevo saldo: ${self._saldo_actual:.2f}.")

    def depositar_monto(self, monto: float) -> str:
        """
        Se sobrescribe el método para depositar dinero (realizar un pago a la cuenta).

        Justificación de la Sobrescritura:
        Un depósito en una cuenta de crédito es un pago que reduce la deuda
        o aumenta un saldo a favor. La lógica base de sumar al saldo es correcta.
      
        """
        if monto <= 0:
            return "Error: El monto del pago debe ser positivo."
        # Llama al método de la clase madre para la lógica de depósito fundamental
        # super().depositar_monto(monto) actualiza self._saldo_actual
        # se devuelve un mensaje que podemos usar o ignorar.
        self._saldo_actual += monto # Realiza el pago
        return f"Pago de ${monto:.2f} recibido para cuenta de crédito. Nuevo saldo: ${self._saldo_actual:.2f}."

    def get_limite_credito(self) -> float:
        """Justificación de método: Permite consultar el límite de crédito."""
        return self._limite_credito

    def get_deuda_actual(self) -> float:
        """Justificación de método: Calcula la deuda actual si el saldo es negativo."""
        return -self._saldo_actual if self._saldo_actual < 0 else 0.0

    def get_disponible_credito(self) -> float:
        """Justificación de método: Calcula el crédito disponible para gastar."""
        # Disponible = Límite de Crédito - Deuda Actual
        # Deuda Actual = -Saldo (si Saldo < 0)
        # Disponible = Límite - (-Saldo) = Límite + Saldo (si Saldo < 0)
        # Si Saldo >= 0, Disponible = Límite + Saldo (porque el saldo positivo se suma al límite)
        return self._limite_credito + self._saldo_actual


    def __str__(self) -> str:
        """
        Se sobrescribe el método para incluir el tipo de cuenta y el límite de crédito.

        Justificación de la Sobrescritura:
        Es necesario para mostrar información completa y específica de la CuentaCredito.
        """
        info_base = super().__str__() # Esto ya incluye Propietario y Saldo Actual
        disponible = self.get_disponible_credito()
        return (f"Tipo: {self.__tipo_cuenta} | {info_base} | "
                f"Límite de Crédito: ${self._limite_credito:.2f} | "
                f"Disponible en Crédito: ${disponible:.2f}")
