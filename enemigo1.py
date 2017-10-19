# -*- coding: utf-8
from pilasengine.actores.actor import pilasengine

pilas = pilasengine.iniciar()

class Enemigo1(pilasengine.actores.Actor):

    def iniciar(self):

        self.imagen = "imagenes/enemigo1.png"
        self.escala = 0.43
        self.x = pilas.azar(-200, 200)
        self.y = 145
        self.radio_de_colision = 50
        self.velocidad = 5
        self.disparos = []
        self._contador_demora = 6
        self.demora_entre_disparos = 30
        self.disparo_doble = True
        self.cuando_elimina_enemigo = False
        self.aprender(pilas.habilidades.PuedeExplotar)
        self.aprender(pilas.habilidades.Disparar)
        pilas.utils.interpolar(self, 'rotacion', 360, duracion=3)
        pilas.utils.interpolar(self, 'escala', 1.5, duracion=20)
        pilas.utils.interpolar(self, 'y', self.altura, duracion=15)
        self.tarea_disparar = pilas.tareas.siempre(3, self.realizar_disparo)

    def actualizar(self):
        if self.escala >= 0.7:  # Elovni tiene un punto de mira que indica que se puede matar
            self.imagen = "enemigo1.png"

        # # El ovni intenta evitar nuestros disparos
        # if self.vida < 7 and self.vida > 2:
        #     pilas.utils.interpolar(self, 'y', pilas.azar(-160, 240), duracion=3)
        #     pilas.utils.interpolar(self, 'x', pilas.azar(-250, 250), duracion=3)

        # def actualizar():
            # self.x = [pilas.azar(-230, 230)], 2
        # pilas.tareas.siempre(1, actualizar)

#     def dispararconclick(self):
#         # "Se invoca cuando se hace click sobre el ovni."
#         if self.vida > 0:
#             self.vida -= 1
#
#         elif self.vida <= 0:
#             self.eliminar()
#             self.pilas.camara.vibrar(1, 0.3)
#             self.tarea_disparar.terminar()
#             self.pilas.actores.Enemigo_Abatido(self.x, self.y)
#
#     def realizar_disparo(self):
#         if self.escala >= 0.8:
#             # Esto hace que cada disparo tenga un angulo de tiro diferente
#             self.aprender("disparar", control=None, municion='MiMunicion',
#                             angulo_salida_disparo=pilas.azar(250, 290))  # , frecuencia_de_disparo =1)
#             self.disparar()
#
# class MiMunicion(pilasengine.actores.Actor):
#     def iniciar(self):
#         self.imagen = "disparos/bola_amarilla.png"
#         self.escala = 0.1
#         self.aprender("puedeexplotar")
#
#     def actualizar(self):
#         self.escala_y += 0.1
#         if self.y == -140:
#             self.eliminar()



pilas.ejecutar()



