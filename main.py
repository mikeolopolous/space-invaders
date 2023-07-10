import pygame
import random

pygame.init()

pantalla = pygame.display.set_mode(
    size=(800, 600)
)

pygame.display.set_caption(
    title="Space Invaders"
)

icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("fondo.jpg")

img_jugador = pygame.image.load("cohete.png")
pos_x_jugador = 368
pos_y_jugador = 520
pos_x_jugador_cambia = 0

img_enemigo = pygame.image.load("enemigo.png")
pos_x_enemigo = random.randint(0, 736)
pos_y_enemigo = random.randint(50, 200)
pos_x_enemigo_cambia = 2
pos_y_enemigo_cambia = 30


def jugador(x, y):
    pantalla.blit(
        source=img_jugador,
        dest=(x, y)
    )


def enemigo(x, y):
    pantalla.blit(
        source=img_enemigo,
        dest=(x, y)
    )


ejecutar = True
while ejecutar:
    # pantalla.fill((34, 87, 122))
    pantalla.blit(fondo, (0, 0))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutar = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                pos_x_jugador_cambia = -2.5
        
            if evento.key == pygame.K_RIGHT:
                pos_x_jugador_cambia = 2.5

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                pos_x_jugador_cambia = 0
    
    pos_x_jugador += pos_x_jugador_cambia
    if pos_x_jugador <= 0:
        pos_x_jugador = 0
    elif pos_x_jugador >= 736:
        pos_x_jugador = 736
    
    pos_x_enemigo += pos_x_enemigo_cambia
    if pos_x_enemigo <= 0:
        pos_x_enemigo_cambia = 2
        pos_y_enemigo += pos_y_enemigo_cambia
    elif pos_x_enemigo >= 736:
        pos_x_enemigo_cambia = -2
        pos_y_enemigo += pos_y_enemigo_cambia

    jugador(pos_x_jugador, pos_y_jugador)
    enemigo(pos_x_enemigo, pos_y_enemigo)
    pygame.display.update()
