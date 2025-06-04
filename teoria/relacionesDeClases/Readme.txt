# Fecha: Mar, 2025.
# Versión: 2.0 (relacionesDeClases)
# Autor: David Gael Osorio Del Olmo (douxvi) o (cyborgael) 
Cliente.py 2.0: Se modificó la clase Cliente para que pueda "tener" un objeto Cuenta. 
Se implementó la importación: from cuenta import Cuenta para que Cliente conozca la clase Cuenta.
Presentación de Atributo __cuenta_asociada: Se añadió este atributo para almacenar el objeto Cuenta del cliente.
También el constructor ahora acepta un parámetro opcional cuenta_bancaria.
Método asignar_cuenta ahora permite asignar o cambiar la cuenta de un cliente después de su creación.
imprimir_detalles_cliente se modificó y ahora también muestra la información de la cuenta asociada, si existe.
Getters: Se añadieron get_nombre y get_cuenta_asociada como ejemplo.

Cuenta. py 2.0: La clase Cuenta permanece estructuralmente igual que en la versión anterior, ya que la relación "Cliente tiene una Cuenta" se modela principalmente desde el Cliente. 
Aún así me aseguré de que el propietario siga siendo un atributo.
Solo como 2 pequeños cambios: El atributo __propietario se renombró a __propietario_cuenta para mayor claridad interna y se añadieron get_saldo y set_saldo.

Menu.py 2.0: Se actualizó la clase Menu añadiendo los métodos para las opciones y el ciclo de validación.
Empezamos por el constructor ya que ahora también toma una cuenta_operable para que el menú sepa sobre qué cuenta actuar.
Se puso __cuenta_actual la cual Almacena la cuenta con la que se trabajará.
Métodos de Opción:
opcion_retirar(): Imprime "-> Está en la opción de Retirar dinero." opcion_depositar(): Imprime "-> Está en la opción de Depositar dinero."
opcion_salir(): Imprime el mensaje de despedida. Por ahora, opcion_retirar y opcion_depositar solo muestran el mensaje. 
desplegar_opciones_principales: Se implementó el ciclo while que muestra las opciones.
Se valida que la entrada sea '1', '2', o '3'.
Llama al método correspondiente o muestra un mensaje de error.
El bucle termina cuando el usuario elige '3' (Salir).

Main.py 2.0: Se modificó para reflejar los cambios en Cliente y Menu. 
Se creó el objeto Cuenta primero al igual que Cliente: Al crear cliente_principal, se pasa a cuenta_principal_virginia para establecer la relación.
Uso de Menu:
Se creó menu_cuenta_cliente pasándo la cuenta del cliente (cliente_principal.get_cuenta_asociada()).
También se llamó a menu_cuenta_cliente.desplegar_opciones_principales() para iniciar el menú interactivo.
