# -*- coding: utf-8
import pilasengine

from espacio import Espacio
from nave import NaveEspacial
from asteroide import Asteroide
from boton import BotonReiniciar
from botonsalir import BotonSalir

pilas = pilasengine.iniciar()

puntaje = pilas.actores.Puntaje(280, 200, color=pilas.colores.blanco)

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
    estrella.rotacion = [-360, 360]

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
    texto = pilas.actores.Texto("GAME OVER (x_x) | Conseguiste %d puntos" %(puntaje.obtener()))
    texto.color = pilas.colores.rojo
    pilas.actores.BotonReiniciar()
    pilas.actores.BotonSalir()

pilas.colisiones.agregar(nave, enemigos, perder)


def nivel_2(enemigos, fondo):
    pilas.avisar("NIVEL 2")
    enemigos.velocidad = pilas.azar(50, 60) / 10.0
    fondo.imagen = "imagenes/espacio_nivel_2.jpg"
    fondo.dy = -8
    pilas.tareas.siempre(0.55, crear_enemigo)

pilas.tareas.agregar(30, nivel_2, enemigos, fondo)


def nivel_3(enemigos, fondo):
    pilas.avisar("NIVEL 3")
    enemigos.velocidad = pilas.azar(50, 60) / 10.0
    fondo.imagen = "imagenes/espacio_nivel_3.jpeg"
    fondo.dy = -12
    pilas.tareas.siempre(0.45, crear_enemigo)

pilas.tareas.agregar(60, nivel_3, enemigos, fondo)


def fin_juego(fondo):
    texto = pilas.actores.Texto("FIN DEL JUEGO")
    texto.color = pilas.colores.blanco
    texto.y = 70
    texto2 = pilas.actores.Texto("Felicitaciones!!! Has obtenido %d puntos" %(puntaje.obtener()))
    texto2.color = pilas.colores.verde
    texto2.y = 35
    fondo.imagen = "imagenes/final.jpg"
    fondo.dy = 0
    nave.eliminar()

pilas.tareas.agregar(90, fin_juego, fondo)


pilas.avisar(u"NIVEL 1")


pilas.actores.vincular(NaveEspacial)
pilas.actores.vincular(Asteroide)
pilas.actores.vincular(BotonReiniciar)
pilas.actores.vincular(BotonSalir)


pilas.ejecutar()
