# Fecha: Mar, 2025.
# Versión: 1.0 (clasesYMetodos)
# Autor: David Gael Osorio Del Olmo (douxvi) o (cyborgael) 
Menu.py: Eencargada de la interacción inicial con el usuario. El presenta el atributo __saludo y se ha hecho privado (convención con __).
Añadí type hints para mejorar la legibilidad (saludo_inicial: str).

Cliente.py: Se define la clase Cliente, que almacenará la información de los usuarios del banco. Los atributos (nombre, direccion y edad) 
se han renombrado para que se vean más acá a (nombre_completo, domicilio, anios_edad) 
y se almacenan como privados (__nombre, __direccion, __edad).
El método imprimirDetalles también se renombró a imprimir_detalles_cliente, aunque tal vez la convención de imprimirDetalles era más práctica, pero para darle sazón. 

Cuenta.py: Aquí se define la clase Cuenta, que gestionará las operaciones bancarias. 
Los atributos (saldo_inicial, tipo_de_cuenta, nombre_propietario) también se han almacenado como privados (__saldo_actual, __tipo_cuenta, __propietario).
Se presentan los métodos imprimir_detalles_cuenta, depositar_monto y retirar_monto. 
También e han añadido:
Saldo inicial no negativo.
Monto de depósito positivo.
Monto de retiro positivo y verificación de fondos insuficientes.
La salida de los métodos depositar_monto y retirar_monto ahora informa el monto de la transacción y el nuevo saldo.
Al igual se usa formateo para mostrar los montos con dos decimales (claro que queremos centavos).

Main.py: Este archivo se utiliza para probar la funcionalidad de las clases creadas. 
Se importan las clases Menu, Cliente y Cuenta.
Se creó una clase MainApp con un método ejecutar para organizar el código de prueba, en lugar de tenerlo directamente en el scope global del script.
Se crean instancias de cada clase y se utilizan sus métodos para demostrar su funcionamiento.
Ya para concluir se incluyó el bloque if __name__ == "__main__".
