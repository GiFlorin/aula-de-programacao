import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definição das cores
branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (0, 255, 0)
vermelho = (255, 0, 0)

# Definição das dimensões da janela do jogo
largura_janela = 800
altura_janela = 600

# Inicialização da janela do jogo
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption('Jogo da Cobrinha')

# Relógio para controle de atualizações de tela
relogio = pygame.time.Clock()

# Definição do tamanho do bloco da cobrinha e da velocidade do jogo
tamanho_bloco = 20
velocidade = 15

# Função para desenhar a cobrinha na tela
def desenhar_cobrinha(lista_cobrinha):
    for bloco in lista_cobrinha:
        pygame.draw.rect(janela, preto, [bloco[0], bloco[1], tamanho_bloco, tamanho_bloco])

# Função do loop principal do jogo
def jogo():
    # Variáveis iniciais da cobrinha
    game_over = False
    game_encerrado = False

    posicao_x = largura_janela / 2
    posicao_y = altura_janela / 2

    delta_x = 0
    delta_y = 0

    lista_cobrinha = []
    tamanho_cobrinha = 1

    # Posição inicial da comida
    comida_x = round(random.randrange(0, largura_janela - tamanho_bloco) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura_janela - tamanho_bloco) / 20.0) * 20.0

    while not game_over:
        while game_encerrado == True:
            janela.fill(branco)
            mensagem_game_over("Fim de Jogo! Pressione C para jogar novamente", vermelho)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_encerrado = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_encerrado = False
                    if event.key == pygame.K_c:
                        jogo()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    delta_x = -tamanho_bloco
                    delta_y = 0
                elif event.key == pygame.K_RIGHT:
                    delta_x = tamanho_bloco
                    delta_y = 0
                elif event.key == pygame.K_UP:
                    delta_y = -tamanho_bloco
                    delta_x = 0
                elif event.key == pygame.K_DOWN:
                    delta_y = tamanho_bloco
                    delta_x = 0

        if posicao_x >= largura_janela or posicao_x < 0 or posicao_y >= altura_janela or posicao_y < 0:
            game_encerrado = True

        posicao_x += delta_x
        posicao_y += delta_y
        janela.fill(branco)
        pygame.draw.rect(janela, verde, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])
        cabeca_cobrinha = []
        cabeca_cobrinha.append(posicao_x)
        cabeca_cobrinha.append(posicao_y)
        lista_cobrinha.append(cabeca_cobrinha)
        if len(lista_cobrinha) > tamanho_cobrinha:
            del lista_cobrinha[0]

        for segmento in lista_cobrinha[:-1]:
            if segmento == cabeca_cobrinha:
                game_encerrado = True

        desenhar_cobrinha(lista_cobrinha)

        pygame.display.update()

        if posicao_x == comida_x and posicao_y == comida_y:
            comida_x = round(random.randrange(0, largura_janela - tamanho_bloco) / 20.0) * 20.0
            comida_y = round(random.randrange(0, altura_janela - tamanho_bloco) / 20.0) * 20.0
            tamanho_cobrinha += 1

        relogio.tick(velocidade)

    pygame.quit()
    quit()

# Função para exibir a mensagem de fim de jogo
def mensagem_game_over(mensagem, cor):
    fonte = pygame.font.SysFont(None, 40)
    texto = fonte.render(mensagem, True, cor)
    janela.blit(texto, [largura_janela / 8, altura_janela / 3])

# Início do jogo
jogo()
