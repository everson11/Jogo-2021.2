import pygame
import time
import random
pygame.init()
largura = 800
altura = 600
configTela = (largura, altura)
gameDisplay = pygame.display.set_mode(configTela)
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
pygame.display.set_caption("CHOVENDO HAMBÚRGUER -By everson ")
icone = pygame.image.load("imagens/chuva-hamburguerpng.png")
pygame.display.set_icon(icone)
sacola = pygame.image.load("imagens/sacola..png")
larguraSacola = 96
fundo = pygame.image.load("imagens/ceu.png")
hamburguer = pygame.image.load("imagens/hamburguer.png")


def login():
    
    nome = input('informe seu nome: ')
    email = input('informe seu email: ')
    dados =  "nome: {} - email: {}.".format(nome, email)
    try:
        open('login.txt', 'r')
    except:
        w = open('login.txt', 'a')
    w = open('login.txt', 'a')
    w.write(dados)
    w.close()
    r = open('login.txt', 'r')
    print(r.read())

def mostraSacola(x, y):
    gameDisplay.blit(sacola, (x, y))

def mostraHamburguer(x, y):
    gameDisplay.blit(hamburguer, (x, y))

def text_objects(texto, font):
    textSurface = font.render(texto, True, black)
    return textSurface, textSurface.get_rect()

def escreverTela(texto):
    fonte = pygame.font.Font("freesansbold.ttf", 115)
    TextSurf, TextRect = text_objects(texto, fonte)
    TextRect.center = ((largura/2, altura/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(5)
    game()

def escreverPlacar(passou, pegou):
    fonte = pygame.font.SysFont(None, 30)
    textoPassou = fonte.render("passou:"+str(passou), True, white)
    textoPegou = fonte.render("pegou:"+str(pegou), True, white)
    gameDisplay.blit(textoPassou, (10, 40))
    gameDisplay.blit(textoPegou, (10, 10))


def game():
    
    sacolaPosicaoX = largura*0.42
    sacolaPosicaoY = altura*0.8
    movimentoX = 0
    velocidade = 20
    hamburguerAltura = 62
    hamburguerLargura = 70
    hamburguerVelocidade = 3
    hamburguerX = random.randrange(0, largura-hamburguerLargura)
    hamburguerY = -200
    passou = 0
    pegou = 0

    login()
    while passou <= 10:
        # pega as ações da tela. Ex.: fechar, click de uma tecla ou do mouse
        acoes = pygame.event.get()  # devolve uma lista de ações
        # [ini] mapeando as ações
        for acao in acoes:
            if acao.type == pygame.QUIT:
                pygame.quit()
                quit()
            if acao.type == pygame.KEYDOWN:
                if acao.key == pygame.K_LEFT:
                    movimentoX = velocidade*-1
                elif acao.key == pygame.K_RIGHT:
                    movimentoX = velocidade
            if acao.type == pygame.KEYUP:
                movimentoX = 0
        # [end] mapeando as ações
        # definindo o fundo do game
        gameDisplay.fill(white)
        gameDisplay.blit(fundo, (0, 0))
        # definindo o fundo do game]
        escreverPlacar(passou,pegou)
        hamburguerY = hamburguerY + hamburguerVelocidade
        mostraHamburguer(hamburguerX, hamburguerY)
        if hamburguerY > altura:
            hamburguerY = -200
            hamburguerX = random.randrange(0, largura)
            hamburguerVelocidade += 0.5
            passou = passou + 1
        sacolaPosicaoX += movimentoX
        if sacolaPosicaoX < 0:
            sacolaPosicaoX = 0
        elif sacolaPosicaoX > largura-larguraSacola:
            sacolaPosicaoX = largura-larguraSacola
        # analise de colisão com o sacolaMan
        if sacolaPosicaoY < hamburguerY + hamburguerAltura:
            ##if sacolaPosicaoX < hamburguerX and sacolaPosicaoX+larguraSacola > hamburguerX or hamburguerX+hamburguerLargura > sacolaPosicaoX and hamburguerX+hamburguerLargura < sacolaPosicaoX+larguraSacola:
            if hamburguerX > sacolaPosicaoX - larguraSacola and hamburguerX < sacolaPosicaoX + larguraSacola:
               hamburguerY = hamburguerY- 600
               hamburguerX = random.randrange(0, largura-hamburguerLargura)
               hamburguerVelocidade += 0.5
               pegou = pegou + 1       
        # analise de colisão com o sacolaMan
        mostraSacola(sacolaPosicaoX, sacolaPosicaoY)
        pygame.display.update()
        clock.tick(60)  # faz com que o while execute 60x por segundo

game()