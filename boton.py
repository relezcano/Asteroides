import pilasengine

import juego

pilas = pilasengine.iniciar()

class BotonReiniciar(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "imagenes/boton_reset.png"
        self.cuando_hace_click = self._reiniciar
        self.y = [190]
        self.x = -280
        self.z = -5
        self.escala = 0.32

    def _reiniciar(self, evento):
        pilas.terminar()
        reload(juego)