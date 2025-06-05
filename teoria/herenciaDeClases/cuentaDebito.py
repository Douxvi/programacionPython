# cuentaDebito.py (Cuenta hija)
# Fecha: May, 2025
# @version: Cyborgael 1.3 
# @autor: Douxvi
from cuenta import Cuenta

class CuentaDebito(Cuenta):
    """
    Representa una cuenta de débito, que es hija de Cuenta por herencia.
    """
    def __init__(self, saldo_inicial: float, propietario: str, limite_extraccion_diario: float = 10000.00):
        """
        Inicializa una cuenta de débito.

        Defs:
            saldo_inicial (float): Saldo inicial. Debe ser >= 0 para débito.
            propietario (str): Nombre del propietario.
            limite_extraccion_diario (float, optional): Límite de retiro por día. Defaults to 10000.00.
        """
        if saldo_inicial < 0:
            # Justificacion: Cuentas de débito no deben iniciar con saldo negativo.
            print(f"Advertencia (Débito - {propietario}): Saldo inicial no puede ser negativo. Se ajustará a 0.")
            saldo_inicial = 0.0
        super().__init__(saldo_inicial, propietario)
        self.__tipo_cuenta = "Debito" # Atributo específico
        # Atributo que justifica el diseño de CuentaDebito: Límite de extracción
        self._limite_extraccion_diario = limite_extraccion_diario
        self._total_retirado_hoy = 0.0 # Para control del límite diario

    def retirar_monto(self, monto: float) -> str:
        """
        Se sobrescribe el método para retirar dinero, aplicando un límite de extracción diario.

        Justificación de la Sobrescritura:
        Las cuentas de débito suelen tener límites diarios de retiro por seguridad
        y para controlar el flujo de efectivo.
        """
        if monto <= 0:
            return "Error: La cantidad a retirar no puede ser negativa."

        # Justificacin de diseño: control de límite diario
        if (self._total_retirado_hoy + monto) > self._limite_extraccion_diario:
            return (f"Error: El monto excede el límite de extracción diario restante. "
                    f"Límite: ${self._limite_extraccion_diario:.2f}, "
                    f"Retirado hoy: ${self._total_retirado_hoy:.2f}, "
                    f"Intenta retirar: ${monto:.2f}")

        # Chequeo de fondos suficientes (propio de débito, no puede sobregirar)
        if self._saldo_actual < monto:
            return "Error: Fondos insuficientes."

        # Si pasa las validaciones específicas de débito, procede con la lógica base.
        # En este caso la lógica base ya hace la resta, pero podríamos optar por 
          no llamar a super() si quisiéramos una lógica de actualización de saldo totalmente diferente.
        # Aquí, llamamos a super() para reutilizar la resta y el formato del mensaje,
        # pero después actualizamos nuestro control de límite.

        # Actualizamos el saldo ANTES de llamar a super() para que el mensaje de super() sea correcto,
        # o llamamos a super() y luego componemos un nuevo mensaje.
        # Por simplicidad, si super().retirar_monto hace la resta,
        # hacemos la validación aquí y si todo OKok, actualizamos nuestros contadores y luego el saldo.

        self._saldo_actual -= monto # Realiza la operación de retiro
        self._total_retirado_hoy += monto
        return (f"Retiro de débito de ${monto:.2f} realizado. "
                f"Nuevo saldo: ${self._saldo_actual:.2f}. "
                f"Total retirado hoy: ${self._total_retirado_hoy:.2f}")

    def depositar_monto(self, monto: float) -> str:
        """
        Se sobrescribe el método para depositar dinero.

        Justificación de la Sobrescritura:
        Aunque la lógica de depósito base es aplicable, podemos añadir detalles o
        comportamientos específicos. En este caso, se personaliza el mensaje
        para confirmar que es un depósito en cuenta de débito y se reutiliza la lógica madre.
        No se añaden reglas funcionales extra sobre el depósito en sí.
        """
        if monto <= 0: # Esta validación ya está en la madre, pero es bueno ser explícito.
            return "Error: El monto a depositar debe ser positivo."
        # Llama al método de la clase madre para la lógica de depósito fundamental
        mensaje_base = super().depositar_monto(monto)
        return f"(Débito) {mensaje_base}" 

    def reset_limite_diario(self):
        """Justificación de método: Permite reiniciar el contador de retiros diarios (simulación)."""
        self._total_retirado_hoy = 0.0
        print(f"Límite de extracción diario reseteado para {self._propietario}.")


    def __str__(self) -> str:
        """
        Sobrescribe el método para incluir el tipo de cuenta y límite de extracción.

        Justificación de la Sobrescritura:
        Es necesario para mostrar información completa y específica de la CuentaDebito.
        """
        info_base = super().__str__()
        return (f"Tipo: {self.__tipo_cuenta} | {info_base} | "
                f"Límite Ret. Diario: ${self._limite_extraccion_diario:.2f} | "
                f"Retirado Hoy: ${self._total_retirado_hoy:.2f}")
