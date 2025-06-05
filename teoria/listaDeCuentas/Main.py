# main.py 3.0
# Fecha: Abr, 2025
# @version: Cyborgael 1.2 
# @autor: Douxvi

from menu import Menu
from cliente import Cliente
from cuenta import Cuenta

class MainApp:
    """
    Clase principal para ejecutar la simulación bancaria.
    Demuestra la gestión de múltiples cuentas por cliente.
    """
    def ejecutar(self):
        """
        Coordina la creación de objetos y la demostración de sus funcionalidades.
        """
        # Crear un Cliente
        # El nombre del propietario ya no se pasa a Cuenta directamente.
        cliente_principal = Cliente(nombre_completo="Virginia Teodosio",
                                    domicilio="Avenida Cyberpunk 2077, Distrito Binario",
                                    anios_edad=40)

        # Crear varias Cuentas
        try:
            cuenta_nomina_vt = Cuenta(saldo_inicial=2500.50, tipo_de_cuenta="nomina")
            cuenta_ahorro_vt = Cuenta(saldo_inicial=12000.75, tipo_de_cuenta="debito") # 'debito' como tipo ahorro
            cuenta_credito_vt = Cuenta(saldo_inicial=500.00, tipo_de_cuenta="credito") # Saldo inicial en crédito podría ser límite o saldo a favor.

            # Agregar las cuentas al Cliente
            cliente_principal.agregar_cuenta(cuenta_nomina_vt)
            cliente_principal.agregar_cuenta(cuenta_ahorro_vt)
            cliente_principal.agregar_cuenta(cuenta_credito_vt)

        except ValueError as ve:
            print(f"Error al crear cuenta: {ve}")
            return # Terminar ejecución si hay error en la creación de cuentas base.


        # Mostrar detalles iniciales del cliente y sus cuentas usando __str__
        print(cliente_principal)


        # Demostrar eliminación de una cuenta (opcional)
        # cliente_principal.eliminar_cuenta(1) # Eliminaría la cuenta de ahorro por índice
        # print("\nCliente después de eliminar una cuenta:")
        # print(cliente_principal)


        # Crear instancia del Menú para el cliente
        menu_banco = Menu(saludo_inicial="Bienvenido(a) al Portal Bancario City Cyborg",
                          cliente_actual=cliente_principal)

        # Iniciar la interacción principal con el menú del cliente
        menu_banco.desplegar_menu_principal_cliente()


        # Estado final de las cuentas del cliente
        print("\n--- Estado Final de Todas las Cuentas ---")
        # cliente_principal.info_cuentas() # O simplemente:
        print(cliente_principal)


if __name__ == "__main__":
    app = MainApp()
    app.ejecutar()
