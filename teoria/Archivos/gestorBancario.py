# gestorBancario.py
# Fecha: Jun, 2025
# @version: Cyborgael 1.4
# @autor: Douxvi

import pickle
import os
from typing import List

# Importar nuestras clases personalizadas
from cliente import Cliente
from cuenta_debito import CuentaDebito
from cuenta_credito import CuentaCredito
# La clase Cuenta base se importa indirectamente a través de sus hijas,
# pero es buenooo tenerla presente si se crean instancias directas.
from cuenta import Cuenta


# Nombre del archivo donde se guardarán los datos
ARCHIVO_DATOS_BANCARIOS = "datosBanco_cityCyborg.pkl"

def cargar_lista_clientes() -> List[Cliente]:
    """
    Se carga la lista de clientes desde el archivo de datos.
    Si el archivo no existe o hay un error, devuelve una lista vacía.
    """
    if os.path.exists(ARCHIVO_DATOS_BANCARIOS):
        try:
            with open(ARCHIVO_DATOS_BANCARIOS, "rb") as f:
                lista_clientes = pickle.load(f)
                print(f"Datos de clientes cargados desde '{ARCHIVO_DATOS_BANCARIOS}'.")
                return lista_clientes
        except (pickle.UnpicklingError, EOFError, AttributeError, ImportError, IndexError) as e:
            print(f"Advertencia: No se pudo cargar el archivo de datos ({e}). Se iniciará con datos vacíos.")
            # Opcional: En sí se podría hacer una copia de seguridad del archivo corrupto aquí
            return []
    else:
        print("Información: Archivo de datos no encontrado. Se iniciará una nueva sesión.")
        return []

def guardar_lista_clientes(clientes: List[Cliente]):
    """
    Se guarda la lista de clientes actual en el archivo de datos.
    """
    try:
        with open(ARCHIVO_DATOS_BANCARIOS, "wb") as f:
            pickle.dump(clientes, f)
            print(f"Datos de clientes guardados en '{ARCHIVO_DATOS_BANCARIOS}'.")
    except pickle.PicklingError as e:
        print(f"Error: No se pudieron guardar los datos de los clientes: {e}")
    except Exception as e:
        print(f"Error inesperado al guardar datos: {e}")


def simular_interaccion_bancaria(clientes_actuales: List[Cliente]):
    """
    Se simula una interacción básica para modificar datos de clientes/cuentas.
    """
    print("\n--- Simulación de Interacción Bancaria ---")
    if not clientes_actuales:
        print("No hay clientes en el sistema para simular interacción.")
        # Podríamos ofrecer crear un nuevo cliente aquí
        nombre_nuevo = input("Ingrese el nombre del nuevo cliente: ")
        domicilio_nuevo = input("Ingrese el domicilio del nuevo cliente: ")
        try:
            edad_nueva = int(input("Ingrese la edad del nuevo cliente: "))
            nuevo_cliente = Cliente(nombre_completo=nombre_nuevo, domicilio=domicilio_nuevo, anios_edad=edad_nueva)
            
            # Añadirle una cuenta de débito por defecto
            cuenta_deb_nueva = CuentaDebito(saldo_inicial=100.0, propietario=nuevo_cliente.get_nombre(), limite_extraccion_diario=500.0)
            nuevo_cliente.agregar_cuenta(cuenta_deb_nueva)
            
            clientes_actuales.append(nuevo_cliente)
            print(f"Cliente {nuevo_cliente.get_nombre()} creado y añadido al sistema.")
        except ValueError:
            print("Edad no válida. No se pudo crear el cliente.")
            return


    # Mostrar todos los clientes y sus cuentas
    print("\nListado de Clientes y sus Cuentas (Antes de operación):")
    if not clientes_actuales:
        print("No hay clientes para mostrar.")
    for idx, cliente_obj in enumerate(clientes_actuales):
        print(f"\n[Cliente {idx}]")
        print(cliente_obj) # Usa el __str__ de Cliente

    # Simular una operación en la primera cuenta del primer cliente, si existe
    if clientes_actuales:
        primer_cliente = clientes_actuales[0]
        print(f"\nOperando con el cliente: {primer_cliente.get_nombre()}")
        cuentas_del_cliente = primer_cliente.get_lista_cuentas()
        if cuentas_del_cliente:
            primera_cuenta = cuentas_del_cliente[0]
            print(f"Operando con la cuenta (antes): {str(primera_cuenta)}")
            
            monto_deposito_simulado = 150.75
            print(f"Simulando depósito de ${monto_deposito_simulado:.2f} en la primera cuenta...")
            print(primera_cuenta.depositar_monto(monto_deposito_simulado))
            
            print(f"Cuenta después del depósito: {str(primera_cuenta)}")
        else:
            print(f"El cliente {primer_cliente.get_nombre()} no tiene cuentas para operar.")
    
    print("\n--- Fin de Simulación de Interacción ---")


if __name__ == "__main__":
    # 1. Cargar datos ANTES de cualquier mensaje de bienvenida del "sistema principal"
    lista_clientes_sistema = cargar_lista_clientes()

    # Mensaje de bienvenida del sistema
    print("\n*** ¡Bienvenido al gestor Bancario City Cyborg! ***")

    # Si no hay clientes cargados (primera ejecución o archivo borrado/corrupto),
    # creamos un cliente de ejemplo para tener algo con qué trabajar.
    if not lista_clientes_sistema:
        print("Iniciando con un cliente de ejemplo (uste maestra).")
        cliente_ejemplo = Cliente(nombre_completo="Virginia Teodosio II",
                                  domicilio="Calle Oro 123, Colonia Binaria",
                                  anios_edad=25)
        try:
            cta_deb_ej = CuentaDebito(saldo_inicial=1200.00,
                                      propietario=cliente_ejemplo.get_nombre(),
                                      limite_extraccion_diario=600.00)
            cta_cred_ej = CuentaCredito(saldo_inicial=50.00, # Saldo a favor
                                       propietario=cliente_ejemplo.get_nombre(),
                                       limite_credito=2500.00)
            cliente_ejemplo.agregar_cuenta(cta_deb_ej)
            cliente_ejemplo.agregar_cuenta(cta_cred_ej)
            lista_clientes_sistema.append(cliente_ejemplo)
        except ValueError as ve:
            print(f"Error creando cuentas de ejemplo: {ve}")


    # Aquí iría la lógica principal de la aplicación,
    # por ejemplo, la interacción con los menús (MenuPrincipal, MenuSecundario).
    # Por ahora, usaremos una simulación simple:
    simular_interaccion_bancaria(lista_clientes_sistema)


    # 2. Al despedirse (finalizar la aplicación), guardar los cambios.
    print("\n*** Finalizando sesión del Gestor Bancario City Cyborg... ***")
    guardar_lista_clientes(lista_clientes_sistema)
    print("¡Gracias por usar nuestros servicios! Datos guardados.")
