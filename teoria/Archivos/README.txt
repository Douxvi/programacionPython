#
#
#
Explicación del archivo gestor bancario: 
Se implementó la persistencia de datos para los clientes y sus cuentas utilizando archivos. Cargando la información al inicio y guardandola al finalizar la sesión.

Para esto, usaremos el módulo pickle de Python, que permite serializar y deserializar objetos Python completos, incluyendo nuestras instancias de clases personalizadas 
(Cliente, CuentaDebito, CuentaCredito).
Se creó un nuevo script principal para esta funcionalidad, llamado, gestorBancario.py. Este script manejará la carga y guardado, y simulará una interacción básica para demostrar los cambios.

Existen algunos requisitos Previos:
Como asegurarnoos de tener los siguientes archivos de la versión "Cyborgael 1.3 - Herencia de Cuentas" en el mismo directorio que el nuevo script:

cuenta.py (Clase Base)
cuenta_debito.py (Clase Hija)
cuenta_credito.py (Clase Hija)
cliente.py (Clase Cliente que maneja una lista de cuentas)

Bien. una vez entendido esto explicaré paso a paso: 
Primero las importaciones:
pickle como ya dijimos sirve para serializar/deserializar objetos.
os sirve para verificar la existencia del archivo (os.path.exists).
List de typing para type hints.
Las clases Cliente, CuentaDebito, CuentaCredito, y Cuenta. Son cruciales que estén disponibles (importables) cuando pickle intente cargar los objetos, de lo contrario, no sabrá cómo reconstruirlos.

ARCHIVO_DATOS_BANCARIOS: Es la constante que define el nombre del archivo donde se almacenarán los datos.

cargar_lista_clientes():
Verifica si ARCHIVO_DATOS_BANCARIOS existe.
Si existe, intenta abrirlo en modo lectura binaria ("rb") y usa pickle.load(f) para deserializar el objeto (que esperamos sea una lista de clientes) del archivo.
Imprime un mensaje de éxito o advertencia si la carga falla (por ejemplo, si el archivo está corrupto o no es un pickle válido). En caso de error, devuelve una lista vacía.
Si el archivo no existe, informa al usuario y devuelve una lista vacía.

guardar_lista_clientes(clientes: List[Cliente]):
Recibe la lista actual de objetos Cliente.
Abre ARCHIVO_DATOS_BANCARIOS en modo escritura binaria ("wb"). El modo "wb" sobrescribirá el archivo si ya existe, lo cual pues es el comportamiento deseado para guardar el estado más reciente.
Usa pickle.dump(clientes, f) para serializar la lista completa de clientes en el archivo.
Este también maneja posibles errores durante el guardado.

simular_interaccion_bancaria(clientes_actuales: List[Cliente]):
Esta función es un placeholder para la lógica principal de la aplicación (que podría involucrar los menús que se desarrollaron anteriormente, adaptados para trabajar con clientes_actuales).
Si no hay clientes, se ofrece crear uno nuevo de forma interactiva.
Muestra los clientes existentes y sus cuentas usando el método __str__ de la clase Cliente.
Realiza una operación de depósito simulada en la primera cuenta del primer cliente para demostrar que los datos se pueden modificar en memoria.

Bloque if __name__ == "__main__": (Flujo Principal)(Lo bueno):
Carga de Datos: Llama a cargar_lista_clientes() antes de cualquier mensaje de bienvenida principal (Como lo pidió). El resultado se almacena en lista_clientes_sistema.
Mensaje de Bienvenida: Muestra un saludo general del sistema.
Datos de Ejemplo (Primera Ejecución): Si lista_clientes_sistema está vacía después de intentar cargar (lo que sucedería la primera vez que se ejecuta el script o si el archivo de datos se elimina/corrompe), 
crea un Cliente de ejemplo con una CuentaDebito y una CuentaCredito y lo añade a la lista. Esto asegura que haya algo de información para ver y guardar en la primera ejecución.
Llamada a la Simulación: Invoca a simular_interaccion_bancaria() pasándole la lista de clientes (que puede ser la cargada o la recién creada con datos de ejemplo).
Guardado de Datos: Al final del script (simulando el "despedirse"), llama a guardar_lista_clientes(lista_clientes_sistema) para persistir cualquier cambio realizado en lista_clientes_sistema durante la sesión.
Ya por último lanza el mensaje de despedida.

