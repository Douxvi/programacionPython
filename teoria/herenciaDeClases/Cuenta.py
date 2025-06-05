# cuenta.py 4.0 (Cuenta madre)
# Fecha: May, 2025
# @version: Cyborgael 1.3
# @autor: Douxvi

class Cuenta:
    """
    Clase base para diferentes tipos de cuentas bancarias.
    """
    def __init__(self, saldo_inicial: float, propietario: str):
        """
        Inicializa una cuenta bancaria base.

        Defs:
            saldo_inicial (float): El saldo inicial de la cuenta.
            propietario (str): El nombre del propietario de la cuenta.
        """
        # El saldo puede ser negativo en ciertos tipos de cuenta (como la de crédito)
        # La validación estricta de saldo inicial >= 0 se relajará aquí
        # y se manejará específicamente en clases hijas si es necesario.
        self._saldo_actual = float(saldo_inicial) # Atributo protegido para acceso en clases hijas
        self._propietario = propietario # Atributo protegido también

    def depositar_monto(self, monto: float) -> str:
        """
        Deposita un monto en la cuenta. Comportamiento base.

        Defs:
            monto (float): La cantidad a depositar. Debe ser positiva.
        Devuelve:
            str: Mensaje indicando el resultado de la operación.
        """
        if monto <= 0:
            return "Error: El monto a depositar debe ser positivo."
        self._saldo_actual += monto
        return f"Depósito de ${monto:.2f} realizado. Nuevo saldo: ${self._saldo_actual:.2f}"

    def retirar_monto(self, monto: float) -> str:
        """
        Retira un monto de la cuenta. Comportamiento base.

        Defs:
            monto (float): La cantidad a retirar. Debe ser positiva.
        Devuelve:
            str: Mensaje indicando el resultado de la operación.
        """
        if monto <= 0:
            return "Error: La cantidad a retirar no puede ser negativa."
        if self._saldo_actual < monto: # Chequeo básico para cuentas con saldo positivo
            return "Error: Fondos insuficientes."
        self._saldo_actual -= monto
        return f"Retiro de ${monto:.2f} realizado. Nuevo saldo: ${self._saldo_actual:.2f}"

    def get_saldo(self) -> float:
        return self._saldo_actual

    def get_propietario(self) -> str:
        return self._propietario

    def __str__(self) -> str:
        """
        Devuelve una representación en cadena base de la cuenta.
        """
        return (f"Propietario: {self._propietario} | "
                f"Saldo Actual: ${self._saldo_actual:.2f}")
