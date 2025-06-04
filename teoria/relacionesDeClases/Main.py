# main.py 2.0
# Fecha: Mar, 2025
# @version: Cyborgael 1.1 
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
        Coordina la creación de objetos y la demostración de sus funcionalidades.
        """
        # Saludo inicial del sistema general 
        print("*** ¡Bienvenido a tu banco Digital City Cyborg! ***")

        # Crear una Cuenta primero
        cuenta_principal_virginia = Cuenta(saldo_inicial=3500.80,
                                           tipo_de_cuenta="Nómina Preferente",
                                           nombre_propietario="Virginia Teodosio")

        # Crear un Cliente y asociarle la Cuenta
        cliente_principal = Cliente(nombre_completo="Virginia Teodosio",
                                    domicilio="Calle Oro 123, Colonia Binaria",
                                    anios_edad=25,
                                    cuenta_bancaria=cuenta_principal_virginia) # Cliente "tiene una" cuenta

        # Mostrar detalles del cliente (que incluirá los de su cuenta)
        cliente_principal.imprimir_detalles_cliente()

        menu_cuenta_cliente = Menu(saludo_inicial=f"Operaciones para {cliente_principal.get_nombre()}",
                                   cuenta_operable=cliente_principal.get_cuenta_asociada())
        menu_cuenta_cliente.dar_saludos() 
        menu_cuenta_cliente.desplegar_opciones_principales() # Iniciar ciclo de opciones del menú

        print("\n--- Simulación Finalizada ---")


if __name__ == "__main__":
    app = MainApp()
    app.ejecutar()
