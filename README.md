# Asteroides

#Asteroides es un juego programado en Python utilizando las librerias de Pilasengine.
#Desarrollado como un trabajo practico para la materia Programación Orientada a Objetos (POO) de la carrera de Sistemas del
instituto Capacitas.

# Las Reglas:

#El movimiento de la nave se realiza utilizando las flechas de dirección del teclado y se puede disparar utilizando la
barra espaciadora.

#Durante el transcurso del juego apareceran cada cierto tiempo una Estrella o una Moneda.
#Al tocar la Estrella con la nave, se le proporcionará a la misma la capacidad de dispara doble.
#Al tocar la Moneda con la nave, se le proporcionará a la misma la capacidad de tener una mayor cadencia de disparos.

# La idea del juego es destruir la mayor cantidad posible de asteroides sin morir. 
# El juego termina cuando la nave impacta contra algún asteroide.


###################################################################################################

# Especificaciones Técnicas:

# Los actores estan divididos en Clases, los actores son:

# Actores personalizados:

- Nave Espacial.
- Asteroide.
- Fondo

# Actores propios de pilas utilizados para este juego:

- Estrella.
- Moneda.

# División de archivos:

#El juego esta dividido en 2 archivos.
#El primer archivo contiene el Menu del juego, con las secciones 'Iniciar Juego', 'Ayuda' y 'Salir'.
Nombre del archivo: menu.py

#El segundo archivo contiene el juego propiamente dicho, con los actores personalizados, las funciones del juego, armas obtenibles, objetos enemigos y de mejoras.
Este archivo es importado al código del menu para relacionar dicho menu con el código del juego. Se utiliza "import juego" en el menu para lograr esto.

# Trabajo realizado por Ramiro Lezcano, 1° año de la carrera de Sistemas, Instituto Capacitas. Profesor: Lucas Passalaqua.
