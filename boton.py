from pilasengine.actores.actor import pilasengine
# import pilasengine
from menu import EscenaMenu

pilas = pilasengine.iniciar()

pilas.escenas.vincular(EscenaMenu)
menu = EscenaMenu(pilas)

class BotonVolver(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "imagenes/boton_volver.png"
        self.cuando_hace_click = self._volver_a_la_escena_inicial
        self.y = [200]
        self.x = -200
        self.escala = 0.5

    def _volver_a_la_escena_inicial(self, evento):
        self.EscenaMenu()

        # self.pilas.escenas.EscenaMenu()