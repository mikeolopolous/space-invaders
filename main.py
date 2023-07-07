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

ejecutar = True
while ejecutar:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutar = False
    
    pantalla.fill((34, 87, 122))
    pygame.display.update()
