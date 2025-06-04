# menu.py
# Fecha: Feb, 2025
# @version: Cyborg 1.0
# @autor: Douxvi

class Menu:
    """
    Clase que gestiona el menú de bienvenida del sistema bancario.
    """
    def __init__(self, saludo_inicial: str):
        """
        Inicializa el menú con un saludo.

        Args:
            saludo_inicial (str): El mensaje de bienvenida para el usuario.
        """
        self.__saludo = saludo_inicial

    def dar_saludos(self):
        """
        Muestra el mensaje de bienvenida configurado.
        """
        print(f"*** {self.__saludo} ***")
