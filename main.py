import pygame

# iniciando o pygame
pygame.init()

# Definindo tamanho janela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("janelio top")

# loop do jogo principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            # atualização da tela
            pygame.display.flip()

