import pygame
import sys

# Inicializa o pygame
pygame.init()

# Configurações da janela
largura = 1530
altura = 800
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo-V1")

# Fonte para o texto
fonte = pygame.font.Font(None, 74)

# Relógio do pygame
clock = pygame.time.Clock()

# Variáveis de tempo
tempo_inicial = pygame.time.get_ticks()  # tempo em milissegundos desde o início

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Calcula o tempo decorrido
    tempo_decorrido = pygame.time.get_ticks() - tempo_inicial

    # Converte para minutos, segundos e milissegundos
    minutos = tempo_decorrido // 60000
    segundos = (tempo_decorrido % 60000) // 1000
    milissegundos = (tempo_decorrido % 1000) // 10  # duas casas

    # Cria o texto formatado
    texto = f"{minutos:02}:{segundos:02}:{milissegundos:3}"
    render = fonte.render(texto, True, (255, 255, 255))

    # Atualiza a tela
    tela.fill((0, 0, 0))
    tela.blit(render, (1300, 10))
    pygame.display.flip()

    # Controla o FPS (60 quadros por segundo)
    clock.tick(30)

# Este é um exemplo simples de um programa Pygame que exibe um contador na tela.
# Ele incrementa o contador a cada frame e o exibe no centro da janela.
# O programa continua rodando até que a janela seja fechada pelo usuário.
