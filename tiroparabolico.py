#Cannon — versión rápida y sin fin:
1) Proyectil y balones (targets) se mueven más rápido.
2) El juego nunca termina: los targets que salen se reposicionan.
"""

from random import randrange
from turtle import *
from freegames import vector

# Estado
ball = vector(-200, -200)    # bola "fuera" cuando no está en vuelo
speed = vector(0, 0)
targets = []

# Parámetros de velocidad (ajusta si quieres aún más rápido)
TARGET_SPEED = 1.5    # antes 0.5
TICK_MS = 30          # antes 50 (menor = más FPS)
GRAVITY = 0.35        # gravedad del proyectil (mantener para física)
LAUNCH_DIV = 12       # antes 25 → proyectil sale más rápido

def tap(x, y):
    """Disparo: coloca la bola y define su velocidad inicial más alta."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        # Aumentamos la velocidad inicial del proyectil
        speed.x = (x + 200) / LAUNCH_DIV
        speed.y = (y + 200) / LAUNCH_DIV

def inside(p):
    """True si p está dentro de la ventana."""
    return -200 < p.x < 200 and -200 < p.y < 200

def draw():
    """Dibuja la bola y los targets."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    """Mueve bola y targets, reposa targets que salgan, juego sin fin."""
    # Spawnear targets de vez en cuando
    if randrange(30) == 0:  # un poco más frecuente que 40
        y = randrange(-150, 150)
        targets.append(vector(200, y))

    # Mover targets más rápido
    for target in targets:
<<<<<<< HEAD
        target.x -= TARGET_SPEED
=======
        target.x -= 0.5
 
 # Reposicionar balones que salen por la izquierda
        if target.x < -200:
            target.x = 200
            target.y = randrange(-150, 150)
>>>>>>> origin/main

    # Física del proyectil
    if inside(ball):
<<<<<<< HEAD
        speed.y -= GRAVITY
=======
        # Reducir la gravedad para que el proyectil sea más rápido
        speed.y -= 0.35  # Cambiado de 0.35 a 0.25 (menos gravedad)
>>>>>>> origin/main
        ball.move(speed)

    # Si la bola sale de pantalla, se resetea para permitir otro disparo
    if not inside(ball):
        ball.x, ball.y = -200, -200
        speed.x = speed.y = 0

    # Colisiones: elimina targets golpeados
    dupe = targets.copy()
    targets.clear()
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)
        else:
            # (Opcional) reponer un target cuando uno es destruido
            targets.append(vector(200, randrange(-150, 150)))

    # Reposicionar targets que salgan (no termina el juego)
    for target in targets:
        if not inside(target):
            target.x = 200
            target.y = randrange(-150, 150)

    draw()

<<<<<<< HEAD
    # Loop continuo
    ontimer(move, TICK_MS)
=======
    # El juego nunca termina - eliminar la condición de retorno
    ontimer(move, 50)  # Cambiado de 50 a 30 (más frames por segundo)
>>>>>>> origin/main

# Setup turtle
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
