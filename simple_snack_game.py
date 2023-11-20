import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
largura, altura = 640, 480
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")

# Cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)

# Configurações da cobra
tamanho_cobra = 10
velocidade_cobra = 10

# Configurações da comida
tamanho_comida = 10

# Classe Cobra
class Cobra:
    def __init__(self):
        self.tamanho = tamanho_cobra
        self.corpos = [[100, 50]]
        self.direcao = 'DIREITA'

    def move(self):
        pass
        # Mover a cobra aqui

# Função para desenhar a cobra
def desenha_cobra(cobra):
    for segmento in cobra.corpos:
        pygame.draw.rect(tela, VERDE, [segmento[0], segmento[1], tamanho_cobra, tamanho_cobra])

# Função para criar comida
def cria_comida():
    return [random.randrange(1, largura//tamanho_comida) * tamanho_comida,
            random.randrange(1, altura//tamanho_comida) * tamanho_comida]

# Desenhar comida
def desenha_comida(posicao):
    pygame.draw.rect(tela, VERMELHO, [posicao[0], posicao[1], tamanho_comida, tamanho_comida])

# Loop principal do jogo
def jogo():
    cobra = Cobra()
    comida = cria_comida()

    clock = pygame.time.Clock()
    rodando = True

    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

        # Movimentação da cobra
        # Movimentação da cobra
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            cobra.direcao = 'ESQUERDA'
        if keys[pygame.K_RIGHT]:
            cobra.direcao = 'DIREITA'
        if keys[pygame.K_UP]:
            cobra.direcao = 'CIMA'
        if keys[pygame.K_DOWN]:
            cobra.direcao = 'BAIXO'

        # Atualizar a posição da cobra
        if cobra.direcao == 'DIREITA':
            cobra.corpos.insert(0, [cobra.corpos[0][0] + tamanho_cobra, cobra.corpos[0][1]])
        elif cobra.direcao == 'ESQUERDA':
            cobra.corpos.insert(0, [cobra.corpos[0][0] - tamanho_cobra, cobra.corpos[0][1]])
        elif cobra.direcao == 'CIMA':
            cobra.corpos.insert(0, [cobra.corpos[0][0], cobra.corpos[0][1] - tamanho_cobra])
        elif cobra.direcao == 'BAIXO':
            cobra.corpos.insert(0, [cobra.corpos[0][0], cobra.corpos[0][1] + tamanho_cobra])

        # Verificar se a cobra comeu a comida
        if cobra.corpos[0] == comida:
            comida = cria_comida()
        else:
            cobra.corpos.pop()

        # Verificar colisões
        for segmento in cobra.corpos[1:]:
            if cobra.corpos[0] == segmento:
                rodando = False

        # Atualizar a tela
        tela.fill(PRETO)
        desenha_cobra(cobra)
        desenha_comida(comida)
        pygame.display.update()

        # Verificar colisão com as bordas
        if cobra.corpos[0][0] >= largura or cobra.corpos[0][0] < 0 or cobra.corpos[0][1] >= altura or cobra.corpos[0][1] < 0:
            rodando = False

        clock.tick(velocidade_cobra)

    pygame.quit()

# Iniciar o jogo
jogo()
