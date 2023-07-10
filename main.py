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
pos_x_cambia = 0


def jugador(x, y):
    pantalla.blit(
        source=img_jugador,
        dest=(x, y)
    )


ejecutar = True
while ejecutar:
    pantalla.fill((34, 87, 122))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutar = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                pos_x_cambia = -2.5
        
            if evento.key == pygame.K_RIGHT:
                pos_x_cambia = 2.5

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                pos_x_cambia = 0
    
    pos_x_jugador += pos_x_cambia
    jugador(pos_x_jugador, pos_y_jugador)
    pygame.display.update()
