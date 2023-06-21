import pygame
from colors import *
from valores import *

pygame.init()

pantalla_inicial = pygame.display.set_mode([PANTALLA_ALTO, PANTALLA_ANCHO]) #type superficie

pygame.display.set_caption("Game1") #nombre de la ventana

timer_time = pygame.USEREVENT # timer
pygame.time.set_timer(timer_time, 100) #esta en milisegundos la unidad de medida

#leer una imagen
# imagen_waifu = pygame.image.load("kaguyita.jpg")
# imagen_waifu = pygame.transform.scale(imagen_waifu, (250, 250))

#texto
fuente_texto = pygame.font.SysFont("Arial", 30)
texto = fuente_texto.render("Kaguya-sama", True, RED4)

while flag_game:

    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_game = False
        
        if evento.type == pygame.USEREVENT:
            if evento.type == timer_time:
                if POSICION_ITEM[1] < PANTALLA_ANCHO + 40:
                    POSICION_ITEM[1] = POSICION_ITEM[1] + 10
                else:
                    POSICION_ITEM[1] = -40

        # if evento.type == pygame.MOUSEBUTTONDOWN:
        #     # print(evento.pos)
        #     POSICION_ITEM = list(evento.pos)

        # if evento.type == pygame.KEYDOWN:
        #     if evento.key == pygame.K_LEFT:
        #         POSICION_ITEM[0] = POSICION_ITEM[0] - 10
        #     if evento.key == pygame.K_RIGHT:
        #         POSICION_ITEM[0] = POSICION_ITEM[0] + 10

    lista_teclas = pygame.key.get_pressed()
    if lista_teclas[pygame.K_LEFT]:
        POSICION_ITEM[0] = POSICION_ITEM[0] - 0.1
    if lista_teclas[pygame.K_RIGHT]:
        POSICION_ITEM[0] = POSICION_ITEM[0] + 0.1

    pantalla_inicial.fill(BLACK)
    pygame.draw.rect(pantalla_inicial, COLOR_GAME_BLUE, (0,450,700,50)) #(cordenada x, cordenada y, ancho, alto)
    pygame.draw.rect(pantalla_inicial, COLOR_GAME_BLUE, (350,0,350,700))
    # pantalla_inicial.blit(imagen_waifu, (360, 0)) #(imagen, (coordenadas), ancho , alto) no le va a dar bola al tamaño que yo le mando
    pantalla_inicial.blit(texto, (360, 300))
    pygame.draw.circle(pantalla_inicial, GREENYELLOW, POSICION_ITEM, 40) #(cordenada x, cordenada y), radio

    pygame.display.flip()

pygame.quit()