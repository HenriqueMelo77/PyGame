import pygame
import sys

# Inicializa o pygame
pygame.init()
largura = 1530
altura = 800
tela = pygame.display.set_mode((largura, altura))   # Define o tamanho da janela
pygame.display.set_caption("Jogo-V1")           # Define o título da janela

background = pygame.image.load("assets/Background-v2.png").convert()
background_redim = pygame.transform.scale(background, (largura, altura))  # Redimensiona a imagem de fundo

# Fonte para o texto
fonte = pygame.font.Font(None, 74)          # Define a fonte e o tamanho do texto

# Relógio do pygame
clock = pygame.time.Clock()              # Cria um relógio para controlar o FPS

# Variáveis de tempo
tempo_inicial = pygame.time.get_ticks()  # tempo em milissegundos desde o início

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Calcula o tempo decorrido
    tempo_decorrido = pygame.time.get_ticks() - tempo_inicial       # em milissegundos

    # Converte para minutos, segundos e milissegundos
    minutos = tempo_decorrido // 60000
    segundos = (tempo_decorrido % 60000) // 1000
    milissegundos = (tempo_decorrido % 1000) // 10  # duas casas

    # Cria o texto formatado
    texto = f"{minutos:02}:{segundos:02}:{milissegundos:02}"        # Formata o tempo como min:s:ms
    render = fonte.render(texto, True, (0, 0, 0))             # Renderiza o texto em branco

    # Atualiza a tela
    tela.fill((0, 0, 0))            # Preenche a tela com preto
    tela.blit(background_redim, (0, 0))    
    tela.blit(render, (1300, 10))   # Desenha o texto na posição (1300, 10)
    # Desenha o fundo na tela
    pygame.display.flip()               # Atualiza a tela

    # Controla o FPS (60 quadros por segundo)
    clock.tick(30)

pygame.quit()