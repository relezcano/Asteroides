# coding=utf-8
import pilasengine

pilas = pilasengine.iniciar()

class EscenaMenu(pilasengine.escenas.Escena):

    def iniciar(self):
        # Contenido de la escena principal: menu, fondo, logo del juego
        pilas.fondos.FondoMozaico("imagenes/espacio.jpg")
        self.menu_inicial()
        self.logo_juego()

    @staticmethod
    def logo_juego():
        # importamos logo desde carpeta imagenes
        imagen = pilas.imagenes.cargar("imagenes/titulo.png")
        logo = pilas.actores.Actor()
        logo.imagen = imagen
        logo.y = 160

    def menu_inicial(self):
        # creamos opciones para el menu
        opciones = [
            ("Iniciar Juego", self.iniciar_juego),
            ("Ver ayuda del juego", self.pantalla_ayuda),
            ("Salir", self.salir_juego)
        ]
        self.menu = self.pilas.actores.Menu(opciones, y=20)

    def iniciar_juego(self):
        #Importamos el codigo del juego desde el archivo juego.py
        import juego

    def pantalla_ayuda(self):
        #Seleccionamos la escena Ayuda.
        self.pilas.escenas.Ayuda()

    def salir_juego(self):
        self.pilas.terminar()


MENSAJE_AYUDA = """
En Asteroides, tienes que controlar una nave 
usando el teclado. El objetivo del juego es 
destruir todas las piedras del espacio disparando.
Para disparar tienes que usar la barra espaciadora 
y para mover la nave puedes usar las flechas de 
direccion del teclado. Si tocas la Estrella 
obtendras un arma doble y si tocas la Moneda 
un arma rapida.

"""


class Ayuda(pilasengine.escenas.Escena):
    "Es la escena que da instrucciones de cómo jugar."

    def iniciar(self):
        pilas.fondos.Fondo("imagenes/ayuda.png")
        self.crear_texto_ayuda()
        self.pulsa_tecla_escape.conectar(self.cuando_pulsa_tecla)

    def crear_texto_ayuda(self):
        self.pilas.actores.Texto("Ayuda", y=200)
        self.pilas.actores.Texto(MENSAJE_AYUDA)
        self.pilas.avisar("Pulsa ESC para regresar")

    def cuando_pulsa_tecla(self, *k, **kw):
        self.pilas.escenas.EscenaMenu()


# Vinculamos las escenas
pilas.escenas.vincular(EscenaMenu)
pilas.escenas.vincular(Ayuda)

#Se inicia la escena
pilas.escenas.EscenaMenu()

pilas.ejecutar()