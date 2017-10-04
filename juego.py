# -*- coding: utf-8
import pilasengine
from pilasengine.fondos.fondo_mozaico import FondoMozaico
from pilasengine.actores.actor import Actor

pilas = pilasengine.iniciar()

puntaje = pilas.actores.Puntaje(280, 200, color=pilas.colores.blanco)

# Actor FONDO -----------------------------------------------------------------
class Espacio(FondoMozaico):
    def iniciar(self):
        self.imagen = "imagenes/espacio1.jpg"
        self.dx = 0
        self.dy = 0
        self.acumulador_x = 0
        self.acumulador_y = 0

    def dibujar(self, painter):
        painter.save()

        x = self.pilas.obtener_escena_actual().camara.x + self.acumulador_x
        y = -self.pilas.obtener_escena_actual().camara.y + self.acumulador_y

        ancho, alto = self.pilas.obtener_area()
        painter.drawTiledPixmap(-ancho / 2, -alto / 2, ancho, alto,
                                self.imagen._imagen,
                                x % self.imagen.ancho(),
                                y % self.imagen.alto())

        painter.restore()

    def actualizar(self):
        self.acumulador_x += self.dx
        self.acumulador_y += self.dy

# -----------------------------------------------------------------------------------

# Actor NAVE-------------------------------------------------------------------------
class NaveEspacial(pilasengine.actores.Actor):

    def iniciar(self, x=0, y=-190):

        self.imagen = "imagenes/nave2.png"
        self.escala = 0.5
        self.x = x
        self.y = y
        self.radio_de_colision = 33
        self.velocidad_x = 0
        self.velocidad_y = 0
        self.velocidad = 5
        self.disparos = []
        self._contador_demora = 6
        self.demora_entre_disparos = 10
        self.disparo_doble = False
        self.cuando_elimina_enemigo = False
        self.aprender(pilas.habilidades.PuedeExplotar)

    def actualizar(self):

        control = self.pilas.control
        self.x += self.velocidad_x
        self.y += self.velocidad_y

        if control.izquierda:
            self.velocidad_x -= self.velocidad
        elif control.derecha:
            self.velocidad_x += self.velocidad
        else:
            self.imagen = self.imagen

        if control.arriba:
            self.velocidad_y += self.velocidad
        elif control.abajo:
            self.velocidad_y -= self.velocidad

        if control.boton:
            self.intenta_disparar()

        self._contador_demora += 1

        # Aplica una desaceleración al movimiento de la nave.
        self.velocidad_x *= 0.5
        self.velocidad_y *= 0.5

    def disparar(self):
        self.intenta_disparar()

    def terminar(self):
        pass

    def intenta_disparar(self):
        if self._contador_demora > self.demora_entre_disparos:
            self._contador_demora = 0
            self.crear_disparo()

    def crear_disparo(self):
        if self.disparo_doble:
            disparo1 = self.pilas.actores.DisparoLaser(x=self.izquierda + 5, y=self.y, rotacion=90)
            self.disparos.append(disparo1)
            disparo1.cuando_se_elimina = self._cuando_elimina_disparo

            disparo2 = self.pilas.actores.DisparoLaser(x=self.derecha - 5, y=self.y, rotacion=90)
            self.disparos.append(disparo2)
            disparo2.cuando_se_elimina = self._cuando_elimina_disparo
            disparo1.z = self.z + 1
            disparo2.z = self.z + 1
        else:
            disparo1 = self.pilas.actores.DisparoLaser(x=self.x, y=self.y, rotacion=90)
            self.disparos.append(disparo1)
            disparo1.z = self.z + 1
            disparo1.cuando_se_elimina = self._cuando_elimina_disparo

    def _cuando_elimina_disparo(self, disparo):
        if disparo in self.disparos:
            self.disparos.remove(disparo)

    def definir_enemigos(self, grupo, cuando_elimina_enemigo=None):
        """Hace que una nave tenga como enemigos a todos los actores del grupo."""
        self.cuando_elimina_enemigo = cuando_elimina_enemigo
        self.pilas.colisiones.agregar(self.disparos, grupo, self.hacer_explotar_al_enemigo)

    def hacer_explotar_al_enemigo(self, mi_disparo, el_enemigo):
        """Es el método que se invoca cuando se produce una colisión 'tiro <-> enemigo'
        """
        mi_disparo.eliminar()
        el_enemigo.eliminar()

        if self.cuando_elimina_enemigo:
            self.cuando_elimina_enemigo()
#------------------------------------------------------------------------

#Actor ASTEROIDE---------------------------------------------------------
class Asteroide(pilasengine.actores.Actor):

    def iniciar(self):
        self.imagen = "imagenes/asteroide.png"
        self.escala = 0.5
        self.aprender( pilas.habilidades.PuedeExplotar )
        self.x = pilas.azar(-200, 200)
        self.y = 300
        self.velocidad = pilas.azar(10, 60) / 10.0

    def actualizar(self):
        self.rotacion += 10
        self.y -= self.velocidad

        # Elimina el objeto cuando sale de la pantalla.
        if self.y < -300:
            self.eliminar()

# Crear el Fondo Personalizado----------------------------------
fondo = Espacio(pilas)
fondo.dy = -5
#---------------------------------------------------------------

# Crear Enemigos (Asteroides)-----------------------------------
enemigos = pilas.actores.Grupo()

def crear_enemigo():
    actor = Asteroide(pilas)
    enemigos.agregar(actor)

pilas.tareas.siempre(0.65, crear_enemigo)
#----------------------------------------------------------------

# Crear Estrella-------------------------------------------------
def crear_estrella():
    estrella = pilasengine.actores.Estrella(pilas)
    estrella.escala = 0.5
    pilas.colisiones.agregar(estrella, nave, asignar_arma_doble)
    estrella.rotacion = [360, -360]

pilas.tareas.siempre(25, crear_estrella)
#-----------------------------------------------------------------

# Crear Moneda-------------------------------------------------
def crear_moneda():
    moneda = pilasengine.actores.Moneda(pilas)
    moneda.escala = 2
    pilas.colisiones.agregar(moneda, nave, asignar_arma_rapida)

pilas.tareas.siempre(63, crear_moneda)
#-----------------------------------------------------------------

# Crear NAVE------------------------------------------------------
nave = NaveEspacial(pilas)
nave.aprender(pilas.habilidades.LimitadoABordesDePantalla)
nave.escala = 0.3
nave.definir_enemigos(enemigos, puntaje.aumentar)
#-----------------------------------------------------------------

def eliminar_estrella(estrella):
    estrella.eliminar()

def asignar_arma_simple():
    nave.disparo_doble = False
    nave.demora_entre_disparos = 10

def asignar_arma_doble(estrella, nave):
    nave.disparo_doble = True
    estrella.eliminar()
    pilas.tareas.siempre(12, asignar_arma_simple)
    pilas.avisar("OBTIENES ARMA DOBLE")

def asignar_arma_rapida(moneda, nave):
    nave.demora_entre_disparos = 1
    moneda.eliminar()
    pilas.tareas.siempre(12, asignar_arma_simple)
    pilas.avisar("OBTIENES ARMA RAPIDA")

def perder(nave, enemigos):

    pilas.colisiones.agregar(nave, enemigos, nave.eliminar)
    pilas.camara.vibrar()
    pilas.camara.vibrar(intensidad=3.5, tiempo=2)
    pilas.avisar("HAS PERDIDO (x_x) | Conseguiste %d puntos" %(puntaje.obtener()))

pilas.colisiones.agregar(nave, enemigos, perder)

pilas.avisar(u"Destruye los asteroides")

pilas.ejecutar()
