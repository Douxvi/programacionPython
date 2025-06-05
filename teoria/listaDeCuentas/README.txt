# Fecha: Abr, 2025.
# Versión: 3.0 (listaDeCuentas)
# Autor: David Gael Osorio Del Olmo (douxvi) o (cyborgael) 
Cuenta.py 3.0: Se añadió el método __str__, la validación de tipos de cuenta 
También e removió el atributo propietario de esta clase,ya que el Cliente será el contenedor principal de esta información
Se añadió una lista de tipos de cuenta permitidos como atributo de clase como TIPOS_DE_CUENTA_VALIDOS.
Con Constructor __init__ ahora se valida que tipo_de_cuenta sea uno de los permitidos.
Se eliminó el parámetro nombre_propietario, ya que la Cuenta ahora no gestiona directamente el nombre del propietario (lo hará Cliente).
Se implementó Método __str__ para devolver una cadena formateada con el tipo y saldo de la cuenta.
imprimir_detalles_cuenta ahora simplemente llama a print(str(self)).
depositar_monto y retirar_monto se modificaron para devolver mensajes de estado, como veremos más adelante Menu.py 3.0 también lo hará.
Se agregó el método get_tipo como getter para el tipo de cuenta.

Cliente.py 3.0: Aquí se modificó Cliente para que maneje una lista de cuentas, se implementarón los nuevos métodos y __str__.
Implementación de atributo __lista_cuentas como reemplazo de __cuenta_asociada. Ya que ahora es una lista para almacenar múltiples objetos Cuenta.
Nuevo constructor __init__ el cual inicializa __lista_cuentas y puede poblarla si se provee una lista inicial. 
Métodos nuevos:
agregar_cuenta para añadir objetos Cuenta a __lista_cuentas.
eliminar_cuenta para eliminar una Cuenta por su índice en la lista.
info_cuentas para listar todas las cuentas del cliente con sus detalles (usando cuenta.__str__()).
imprimir_detalles_cliente ahora llama a print(str(self)) para usar la nueva representación.
Igual se añadió get_lista_cuentas y __str__ para mostrar los datos del cliente y un listado de todas sus cuentas.

Menu.py 3.0: El menú ahora interactúa con un cliente que puede tener múltiples cuentas también permitirá seleccionar una cuenta para operar 
las operaciones de retiro/depósito son funcionales.
Nuevo constructor __init__ este ahora toma un objeto Cliente en lugar de una Cuenta individual.
__cuenta_seleccionada es un nuevo atributo para mantener la Cuenta específica con la que el usuario elige operar.
seleccionar_cuenta_operable es un nuevo método que: Muestra las cuentas del cliente (usando cliente.info_cuentas()), Permite al usuario elegir una cuenta por su índice.
y por último también actualiza self.__cuenta_seleccionada.
opcion_retirar y opcion_depositar ahora son completamente funcionales, verifican si hay una __cuenta_seleccionada, solicitan al usuario la cantidad 
También llaman a los métodos retirar_monto o depositar_monto de la __cuenta_seleccionada, muestran el mensaje devuelto por la operación e incluyen manejo básico de ValueError para la entrada de cantidad.
La opcion_salir ahora, al salir de las operaciones de una cuenta, deselecciona la cuenta (self.__cuenta_seleccionada = None).
desplegar_menu_principal_cliente es un nuevo método que actúa como el menú de nivel superior para el cliente, permitiéndole elegir entre seleccionar una cuenta para operar, ver todas sus cuentas o salir del sistema.
desplegar_opciones_de_cuenta_actual se renombró desde desplegar_opciones_principales y ahora es el submenú que se muestra después de que una cuenta ha sido seleccionada. 
El bucle continúa mientras self.__cuenta_seleccionada no sea None. 
La opción "Salir" de este submenú ahora lo lleva de regreso al menú de selección de cuenta.

Main.py 3.0: Este archivo demuestra la nueva estructura con múltiples cuentas por cliente y el flujo del menú mejorado.
Creación de Cliente y Cuentas:
Se crea un Cliente sin pasarle cuentas inicialmente. Se crean varios objetos Cuenta (nómina, débito/ahorro, crédito). Estas cuentas se añaden al Cliente usando el método agregar_cuenta.
 __str__ muestra la información del cliente (que ahora incluye todas sus cuentas) simplemente haciendo print(cliente_principal).
Ahora se pasa el objeto cliente_principal al constructor del Menu.
Se llama menu_banco.desplegar_menu_principal_cliente() para iniciar la interacción. Este método internamente manejará la selección de cuenta y luego mostrará el menú de operaciones para la cuenta seleccionada.
Ya por último el manejo de ValueError el cual añade un bloque try-except durante la creación de cuentas por si se usa un tipo inválido.

