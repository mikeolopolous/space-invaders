import pygame

pygame.init()

pantalla = pygame.display.set_mode(
    size=(800, 600)
)

ejecutar = True
while ejecutar:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutar = False
