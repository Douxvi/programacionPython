# pruebasCuentas.py
# Fecha: May, 2025
# @version: Cyborgael 1.3
# @autor: Douxvi

from cuenta import Cuenta
from cuenta_debito import CuentaDebito
from cuenta_credito import CuentaCredito

def ejecutar_pruebas_de_cuentas():
    """
    Se crean instancias de diferentes tipos de cuentas, se agregan a una lista
    y se prueban sus funcionalidades de forma polimórfica y específica.
    """
    print("##### INICIO DE PRUEBAS DE HERENCIA EN CUENTAS #####\n")

    # 1. Crear al menos 3 objetos (uno de cada clase relevante)
    # Usaremos "Don Pollo" como nombre genérico para estas pruebas directas.
    cuenta_generica = Cuenta(saldo_inicial=500.00, propietario="Don Pollo")
    cuenta_principal_debito = CuentaDebito(
        saldo_inicial=2000.00,
        propietario="Don Pollo Débito",
        limite_extraccion_diario=800.00 # Límite más restrictivo para la prueba
    )
    cuenta_principal_credito = CuentaCredito(
        saldo_inicial=0.00, # Comienza sin deuda ni saldo a favor
        propietario="Don Pollo Crédito",
        limite_credito=1500.00
    )

    # 2. Agregar a una lista
    lista_de_todas_las_cuentas = [cuenta_generica, cuenta_principal_debito, cuenta_principal_credito]

    # 3. Probar cada objeto desde la lista
    for i, cuenta_actual in enumerate(lista_de_todas_las_cuentas):
        print(f"\n--- [{i+1}] Probando Cuenta de Tipo: {cuenta_actual.__class__.__name__} ---")
        print("ESTADO INICIAL:")
        print(cuenta_actual) # Prueba __str__ polimórfica

        # Pruebas comunes de depósito
        print("\n-> Pruebas de Depósito:")
        print(f"Intentando depositar $200.00:")
        print(cuenta_actual.depositar_monto(200.00))
        print(f"Intentando depositar $-50.00 (inválido):")
        print(cuenta_actual.depositar_monto(-50.00))
        print(f"Saldo actual post-depósitos: ${cuenta_actual.get_saldo():.2f}")

        # Pruebas comunes de retiro
        print("\n-> Pruebas de Retiro Comunes:")
        print(f"Intentando retirar $100.00:")
        print(cuenta_actual.retirar_monto(100.00))
        print(f"Saldo actual post-retiro: ${cuenta_actual.get_saldo():.2f}")
        print(f"Intentando retirar $-20.00 (inválido):")
        print(cuenta_actual.retirar_monto(-20.00))

        # Pruebas específicas según el tipo de cuenta
        if isinstance(cuenta_actual, CuentaDebito):
            print("\n-> Pruebas Específicas para CuentaDebito:")
            # Saldo actual de Débito: 2000 (inicial) + 200 (dep) - 100 (ret) = 2100
            # Límite diario: 800. Retirado hoy: 0 (antes de esta prueba específica)
            print(f"Intentando retirar $700.00 (dentro del límite diario de ${cuenta_actual._limite_extraccion_diario:.2f}):")
            print(cuenta_actual.retirar_monto(700.00)) # Retirado hoy: 700
            print(f"Intentando retirar $150.00 más (excedería límite diario de ${cuenta_actual._limite_extraccion_diario:.2f}):")
            print(cuenta_actual.retirar_monto(150.00)) # Debería fallar por límite
            print(f"Total retirado hoy (Débito): ${cuenta_actual._total_retirado_hoy:.2f}")
            cuenta_actual.reset_limite_diario() # Probando método específico

        elif isinstance(cuenta_actual, CuentaCredito):
            print("\n-> Pruebas Específicas para CuentaCredito:")
            # Saldo actual de Crédito: 0 (inicial) + 200 (dep/pago) - 100 (ret/gasto) = 100
            # Límite crédito: 1500. Disponible: 1500 + 100 = 1600
            print(f"Crédito disponible actual: ${cuenta_actual.get_disponible_credito():.2f}")
            print(f"Deuda actual: ${cuenta_actual.get_deuda_actual():.2f}")
            print(f"Intentando gastar $1200.00 con crédito:")
            # Nuevo saldo: 100 - 1200 = -1100. Esto es > -1500 (límite), así que debería ser posible.
            print(cuenta_actual.retirar_monto(1200.00)) # Gastando
            print(f"Saldo post-gasto: ${cuenta_actual.get_saldo():.2f}")
            print(f"Crédito disponible ahora: ${cuenta_actual.get_disponible_credito():.2f}") # Debería ser 1500 - 1100 = 400
            print(f"Deuda actual: ${cuenta_actual.get_deuda_actual():.2f}") # Debería ser 1100
            print(f"Intentando gastar $500.00 más (excedería límite):")
            # Saldo -1100. Disponible 400. Gasto de 500 no debería ser posible.
            print(cuenta_actual.retirar_monto(500.00))

        # Prueba de retiro de un monto muy grande (para fondos insuficientes/límite)
        print("\n-> Prueba de Retiro Elevado:")
        gran_monto_retiro = 50000.00
        print(f"Intentando retirar ${gran_monto_retiro:.2f}:")
        print(cuenta_actual.retirar_monto(gran_monto_retiro))

        print("\nESTADO FINAL de la cuenta:")
        print(cuenta_actual) # Prueba __str__ polimórfica final
        print("--------------------------------------------------")

    print("\n##### FIN DE PRUEBAS DE HERENCIA EN CUENTAS #####")

if __name__ == "__main__":
    ejecutar_pruebas_de_cuentas()
