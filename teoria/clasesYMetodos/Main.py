# main.py
# Fecha: Feb, 2025
# @version: Gaelinicyb 1.0
# @autor: Douxvi

from menu import Menu
from cliente import Cliente
from cuenta import Cuenta

class MainApp:
    """
    Clase principal para ejecutar la simulación bancaria.
    """
    def ejecutar(self):
        """
        Creación de objetos y la demostración de sus funcionalidades.
        """
        # Crear instancia del Menú y dar bienvenida
        menu_banco = Menu(saludo_inicial="¡Bienvenido al Banco Digital Citycyborg!")
        menu_banco.dar_saludos()

        # Crear instancia de Cliente
        cliente_uno = Cliente(nombre_completo="virginia teodosio",
                              domicilio="Calle Oro 123, Ciudad Capital",
                              anios_edad=25)
        cliente_uno.imprimir_detalles_cliente()

        # Cresr instancia de Cuenta para el cliente
        cuenta_virginia = Cuenta(saldo_inicial=15000.75,
                            tipo_de_cuenta="Ahorros Premium",
                            nombre_propietario=cliente_uno._Cliente__nombre) # Acceso demostrativo al nombre del cliente
        cuenta_virginia.imprimir_detalles_cuenta()

        # Operaciones en la cuenta
        print("\n--- Operaciones Bancarias ---")
        cuenta_virginia.depositar_monto(500.25)
        cuenta_virginia.retirar_monto(200.00)
        cuenta_virginia.retirar_monto(2500.00) # Intento de retiro mayor al saldo
        cuenta_virginia.depositar_monto(-50.00) # Intento de depósito negativo

        # Mostrar detalles finales
        print("\n--- Estado Final de la Cuenta ---")
        cuenta_virginia.imprimir_detalles_cuenta()

if __name__ == "__main__":
  # se implementa aquí como 'MainApp' para evitar confusión con el nombre del archivo okkok.
    app = MainApp()
    app.ejecutar()
