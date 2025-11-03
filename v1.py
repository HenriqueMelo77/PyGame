import pygame
import sys

# Inicializa o pygame
pygame.init()
fundo = pygame.image.load("fundo pygame.png").convert_alpha  # Carrega a imagem de fundo
fundo_redim = pygame.transform.scale(fundo, (1530, 800))  # Redimensiona a imagem de fundo
# Configurações da janela
largura = 1530
altura = 800
tela = pygame.display.set_mode((largura, altura))   # Define o tamanho da janela
pygame.display.set_caption("Jogo-V1")           # Define o título da janela

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
    render = fonte.render(texto, True, (255, 255, 255))             # Renderiza o texto em branco

    # Atualiza a tela
    tela.fill((0, 0, 0))            # Preenche a tela com preto
    tela.blit(render, (1300, 10))   # Desenha o texto na posição (1300, 10)
    pygame.display.flip()               # Atualiza a tela
    tela.blit(fundo_redim, (0, 0))         # Desenha o fundo na posição (0, 0)
    # Controla o FPS (60 quadros por segundo)
    clock.tick(30)


