import pilasengine

pilas = pilasengine.iniciar()

class BotonSalir(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "imagenes/botoncerrar.png"
        self.cuando_hace_click = self._salir
        self.y = [190]
        self.x = -280
        self.z = -5
        self.escala = 0.3

    def _salir(self, evento):
        self.pilas.terminar()
        exit()
