# Fecha: May, 2025.
# Versión: 4.0 (herenciaDeClases)
# Autor: David Gael Osorio Del Olmo (douxvi) o (cyborgael) 
cuenta.py 4.0 (Clase Madre)
La clase Cuenta ahora servirá como base progenitora madre de dios
Como primer cambio tenemos los atributos Protegidos en _saldo_actual y _propietario se marcan como protegidos, para indicar que pueden ser accedidos por clases hijas.
Se reintroduce el atributo _propietario.
Constructor __init__ se simplifica para la clase base. La validación estricta de saldo inicial no negativo se mueve a las clases hijas si es pertinente (como en CuentaDebito).
Se mantiene una validación básica de fondos insuficientes como retirar_monto el cual será adaptada o extendida en CuentaCredito.
Se incluye __str__ ya que proporciona una representación base que las clases hijas pueden extender.

cuentaDebito.py (Nueva Clase Hija)
Heredera de su mamá Cuenta y añade lógica específica para cuentas de débito.
Se usa class CuentaDebito(Cuenta) para heredar
La función de __init__ hace varias cosas como: Llamar a super().__init__(), establecer self.__tipo_cuenta = "Debito" y asegurar que el saldo_inicial no sea negativo.
También _limite_extraccion_diario y _total_retirado_hoy se agregan para controlar los retiros diarios.
retirar_monto (fue sobrescrito):
Justificación: Implementa la lógica del límite de extracción diario antes de verificar fondos o realizar el retiro. No llama a super().retirar_monto() 
para tener control total sobre la operación y el mensaje, pero sí realiza la operación de resta del saldo.
depositar_monto (También sobrescrito):
Justificación: Principalmente para personalizar el mensaje. Reutiliza la lógica de la mamá con super().depositar_monto().
reset_limite_diario es un método específico para CuentaDebito que justifica su diseño (manejo de límites diarios).
No podía faltar __str__ (Igual sobrescrito):
Justificación: Extiende la información de la clase base para incluir el tipo "Debito" y los detalles del límite de extracción.

cuentaCredito.py (La otra clase hija)
También es heredera de su mamá Cuenta y añade lógica para cuentas de crédito.
Se usa class CuentaCredito(Cuenta) para heredar
Las funciones de __init__ son las mismas que en débito pero de forma homologa para crédito
Aunque aquí _limite_credito se usa para definir cuánto puede endeudarse el cliente.
retirar_monto (Sobrescrito):
Justificación: Permite que el saldo (_saldo_actual) se vuelva negativo, pero solo hasta el _limite_credito. El "retiro" aquí es conceptualizado como un "gasto".
depositar_monto (Sobrescrito):
Justificación: Un "depósito" es un "pago". La lógica de sumar al saldo es correcta (reduce la deuda o aumenta el saldo a favor). Se personaliza el mensaje.
Métodos Adicionales: Se usan: get_limite_credito, get_deuda_actual, get_disponible_credito.
Justificación: Estos métodos proporcionan información relevante y específica para una cuenta de crédito, como el límite total, la deuda actual (si la hay), y cuánto crédito queda disponible
justificando el diseño especializado de esta clase.
A estás alturas no sorprende que esté __str__ sobrescrito ya que muestra información vital como el tipo "Credito", el límite y el crédito disponible, además de la información base.

PruebasCuentas.py: Es un script de pruebas para los objetos de las clases de cuentas que hemos definido (Cuenta, CuentaDebito, CuentaCredito). Este script instanciará un objeto de cada una, los agregará a una lista y luego iterará sobre la lista para probar sus métodos, incluyendo los que han sido sobrescritos y los específicos de cada subclase.
