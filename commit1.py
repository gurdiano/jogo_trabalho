import pygame
import sys
import os
from pygame.locals import *
from random import randint

# Inicialização do Pygame
pygame.init()

# Configuração da janela
largura = 1366
altura = 768
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo de Aventura')

# Cores
PRETO = (0, 0, 0)

# Dir da Sprtie
sprite_path = r'C:\Users\Tiago\Desktop\notes\Estudos\Python\trabalho\Sprite\Naruto'
correndo1 = '1597674554117.png'
correndo2 = '1597674534838.png'
correndo3 = '1597674579476.png'
chakra = 'imagens-de-aura-png-6.png'

naruto_correndo1 = os.path.join(sprite_path, correndo1)
naruto_correndo2 = os.path.join(sprite_path, correndo2)
naruto_correndo3 = os.path.join(sprite_path, correndo3)
ponto_chakra = os.path.join(sprite_path, chakra)


# Carregar e redimensionar sprites do personagem
def carregar_e_redimensionar(imagem, nova_largura, nova_altura):
    sprite = pygame.image.load(imagem)
    return pygame.transform.scale(sprite, (nova_largura, nova_altura))

sprites_correndo_direita = [carregar_e_redimensionar(naruto_correndo1, 100, 100),  # Ajuste as dimensões conforme necessário
                    carregar_e_redimensionar(naruto_correndo3, 100, 100),
                    carregar_e_redimensionar(naruto_correndo2, 100, 100)]  # Ajuste as dimensões conforme necessário

sprites_ponto_chakra = carregar_e_redimensionar(ponto_chakra, 50, 50)

# Carregar e redimensionar sprites do personagem espelhados
sprites_correndo_esquerda = [pygame.transform.flip(sprite, True, False) for sprite in sprites_correndo_direita]

# Rotaciona sprite em 90°
sprites_correndo_cima = [pygame.transform.rotate(sprite, 90) for sprite in sprites_correndo_direita]

# Rotaciona sprite em 90°
sprites_correndo_baixo = [pygame.transform.rotate(sprite, 90) for sprite in sprites_correndo_esquerda]

indice_sprite = 0
personagem = sprites_correndo_direita[indice_sprite]
bolinha = sprites_ponto_chakra

# Posição e velocidade do personagem
x = 50
y = 10
velocidade = 50

# Posição da bolinha
x1 = randint(40, 1300)
y1 = randint(50, 700)

# Contador para controlar a velocidade da animação
contador_animacao = 0
velocidade_animacao = 3 # Quanto maior, mais lenta a animação


# Variável para controlar a direção atual
direcao = 0

# Relógio para controlar a taxa de atualização
relogio = pygame.time.Clock()

# Inicialize o Rect do personagem e da bolinha
rect_personagem = pygame.Rect(x, y, 100, 100)  # O tamanho deve corresponder ao tamanho do sprite do personagem
rect_bolinha = pygame.Rect(50, 10, 50, 50)  # O tamanho deve corresponder ao tamanho do sprite da bolinha


# Loop principal do jogo
while True:
    relogio.tick(30)  # 30 quadros por segundo

    # Atualize a posição dos Rects baseado na posição do personagem e da bolinha
    rect_personagem.x = x
    rect_personagem.y = y

    rect_bolinha.x = x1
    rect_bolinha.y = y1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas_pressionadas = pygame.key.get_pressed()

    if teclas_pressionadas[K_d]:
        direcao = 0
        contador_animacao += 1
        if contador_animacao >= velocidade_animacao:
            indice_sprite += 1
            if indice_sprite >= len(sprites_correndo_direita):
                indice_sprite = 0
            contador_animacao = 0
        x += velocidade

    elif teclas_pressionadas[K_a]:
        direcao = 1
        contador_animacao += 1
        if contador_animacao >= velocidade_animacao:
            indice_sprite += 1
            if indice_sprite >= len(sprites_correndo_esquerda):
                indice_sprite = 0
            contador_animacao = 0
        x -= velocidade

    if teclas_pressionadas[K_s]:
        direcao = 2
        contador_animacao += 1
        if contador_animacao >= velocidade_animacao:
            indice_sprite += 1
            if indice_sprite >= len(sprites_correndo_direita):
                indice_sprite = 0
            contador_animacao = 0
        y += velocidade

    elif teclas_pressionadas[K_w]:
        direcao = 3
        contador_animacao += 1
        if contador_animacao >= velocidade_animacao:
            indice_sprite += 1
            if indice_sprite >= len(sprites_correndo_cima):
                indice_sprite = 0
            contador_animacao = 0
        y -= velocidade

    # Atualiza o sprite baseado na direção
    if direcao == 1:
        personagem = sprites_correndo_esquerda[indice_sprite]
    elif direcao == 0:
        personagem = sprites_correndo_direita[indice_sprite]
    elif direcao == 2:
        personagem = sprites_correndo_baixo[indice_sprite]
    elif direcao == 3:
        personagem = sprites_correndo_cima[indice_sprite]

    if rect_personagem.colliderect(rect_bolinha):
        x1 = randint(40, 1300)
        y1 = randint(50, 700)

    # Limpa a tela
    tela.fill(PRETO)

    tela.blit(personagem, (rect_personagem.x, rect_personagem.y))
    tela.blit(bolinha, (x1, y1))

    # Atualiza a tela
    pygame.display.flip()
