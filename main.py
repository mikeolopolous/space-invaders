import pygame

pygame.init()

pantalla = pygame.display.set_mode(
    size=(800, 600)
)

pygame.display.set_caption(
    title="Space Invaders"
)

icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)

img_jugador = pygame.image.load("cohete.png")
pos_x_jugador = 368
pos_y_jugador = 536


def jugador():
    pantalla.blit(
        source=img_jugador,
        dest=(pos_x_jugador, pos_y_jugador)
    )


ejecutar = True
while ejecutar:
    pantalla.fill((34, 87, 122))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutar = False
    
    jugador()
    pygame.display.update()
