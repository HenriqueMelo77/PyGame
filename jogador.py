import pygame
import sys

pygame.init()
largura = 1530
altura = 800
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo-V1")

background = pygame.image.load("Background-v2.png").convert()
background_redim = pygame.transform.scale(background, (largura, altura))

fonte = pygame.font.Font(None, 74)
clock = pygame.time.Clock()

tempo_inicial = pygame.time.get_ticks()

altura_jog = 60
largura_jog = 40
cor_jog = (200, 30, 30)

x_jog = 200
base_chao = 170
altura_chao = altura - base_chao - altura_jog  # posição y do topo do jogador quando estiver no chão
chao = altura_chao                                # chao agora é numérico (y do chão)
y_jog = chao                                      # começar no chão

velocidade_jog = 6
velocidade_y_jog = 0

gravidade = 1
pulo_jog = 20    # ajusta se quiser pulo mais alto/baixo
no_chao = True

jogador_surf = pygame.Surface((largura_jog, altura_jog))
jogador_surf.fill(cor_jog)

#loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and no_chao:
                velocidade_y_jog = -pulo_jog
                no_chao = False
            if event.key == pygame.K_c:   # teleporte para o chão
                y_jog = chao
                velocidade_y_jog = 0
                no_chao = True

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x_jog -= velocidade_jog
    if teclas[pygame.K_RIGHT]:
        x_jog += velocidade_jog

    velocidade_y_jog += gravidade
    y_jog += velocidade_y_jog

    if y_jog >= chao:
        y_jog = chao
        velocidade_y_jog = 0
        no_chao = True

    # impedir sair da tela horizontal
    if x_jog < 0:
        x_jog = 0
    if x_jog + largura_jog > largura:
        x_jog = largura - largura_jog

    # Converte para minutos, segundos e milissegundos
    tempo_decorrido = pygame.time.get_ticks() - tempo_inicial
    minutos = tempo_decorrido // 60000
    segundos = (tempo_decorrido % 60000) // 1000
    milissegundos = (tempo_decorrido % 1000) // 10
    texto = f"{minutos:02}:{segundos:02}:{milissegundos:02}"
    render = fonte.render(texto, True, (0, 0, 0))  # Renderiza o texto em branco

    # Atualiza a tela
    tela.fill((0, 0, 0))  # Preenche a tela com preto
    tela.blit(background_redim, (0, 0))
    tela.blit(jogador_surf, (int(x_jog), int(y_jog)))
    tela.blit(render, (1300, 10))
    
    # Desenha o fundo na tela
    pygame.display.flip() # Atualiza a tela
    
    # Controla o FPS (60 quadros por segundo)
    clock.tick(60)  # 60 FPS

pygame.quit()