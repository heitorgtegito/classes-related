import pygame
import random
import sys
import math

# =========================================================
# Iniciozinho basico do pygame
# =========================================================
pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Versão beta do dungeon loop ai")

clock = pygame.time.Clock()
font = pygame.font.Font('Imagens/Fonte.ttf', 24)

# =========================================================
# Controle do status do jogo
# =========================================================
STATE_TITLE = "TITLE"
STATE_DUNGEON = "DUNGEON"
STATE_COMBAT = "COMBAT"
STATE_LEVEL_UP = "LEVEL_UP"
STATE_GAMEOVER = "GAMEOVER"
STATE_POTION_MENU = "POTION_MENU"

state = STATE_TITLE
inicio = True
# =========================================================
# IMPORTANDO IMAGENS
# =========================================================
# =========================================================
# =========================================================
# Geral
# =========================================================
setinha = pygame.image.load("Imagens/Setinha.png").convert()
# =========================================================
# Tela inicial (IMAGENS) --> PRECISA TER NA VERSÃO PARCIAL MLK
# =========================================================
title_bg = pygame.image.load("Imagens/Jogar.png").convert() # Professor tinha dito q o .convert() era bom né, vo botar
botao_jogar = pygame.image.load("Imagens/BotaoJogar.png").convert()
# Centralizar botão
botao_rect = botao_jogar.get_rect()
botao_rect.center = (930, 375) #eu amo .get_rect()
# =========================================================
# Tela de Dungeon -> Exploração
# =========================================================
todas_salas = pygame.image.load("Imagens/SalasSpriteSheet.png").convert()
mascara_salas = pygame.image.load("Imagens/MascaraSalas.png").convert()

def pode_andar(pos):
    x = int(pos.x)
    y = int(pos.y)

    if x < 0 or y < 0 or x >= mascara_salas.get_width() or y >= mascara_salas.get_height():
        return False

    cor = mascara_salas.get_at((x, y))
    return cor.r > 200  # branco = pode andar

# mesa = pygame.image.load("Imagens/MesaSozinha.png").convert() Não acho que vá entrar por agora, quando eu atualizar o jogo pós entrega final eu coloco
# armor_stand = pygame.image.load("Imagens/ArmorStand.png").convert() Mesma coisa q a mesa, nao entra por agora

sprites_personagem = pygame.image.load("Imagens/SpritesPlayer/SpriteSheet_Personagem.png").convert_alpha()
def get_sprite(sheet, x_inicio, x_fim, altura, y_inicio=0): # To usando 2 funções diferentes pq as imagens dos bonecos sao desalinhas
    largura = x_fim - x_inicio
    image = pygame.Surface((largura, altura), pygame.SRCALPHA) # o parâmetro pygame.SRCALPHA indica um surface com fundo transparente
    image.blit(sheet, (0, 0), (x_inicio, y_inicio, largura, altura))
    return image

# Personagem andando -> 17-52px ; 57-90px ; 95-130px ; 140-172px ; 177-210px ; 215-247px ; 260-292px ; 298-330px ; 336-368px ; 
state_jogador = 'frente'

protagonista_baixo1 = get_sprite(sprites_personagem, 17, 52, 64).convert_alpha() # Perna direita na frente
protagonista_baixo2 = get_sprite(sprites_personagem, 57, 90, 64).convert_alpha() # Duas pernas alinhadas
protagonista_baixo3 = get_sprite(sprites_personagem, 95, 130, 64).convert_alpha() # Perna esquerda na frente

protagonista_frente1 = get_sprite(sprites_personagem, 140, 172, 64).convert_alpha() # Perna direita na frente
protagonista_frente2 = get_sprite(sprites_personagem, 177, 210, 64).convert_alpha() # Duas pernas alinhadas
protagonista_frente3 = get_sprite(sprites_personagem, 215, 247, 64).convert_alpha() # Perna esquerda na frente

# No caso desses sprites do lado, vai precisar fazer aquela coisa de inverter pra quando ele tiver indo pra direita, já q os sprites são só pra esquerda
protagonista_lado1 = get_sprite(sprites_personagem, 260, 292, 64).convert_alpha() # Perna esquerda na frente
protagonista_lado2 = get_sprite(sprites_personagem, 298, 330, 64).convert_alpha() # Duas pernas alinhadas
protagonista_lado3 = get_sprite(sprites_personagem, 336, 368, 64).convert_alpha() # Perna direita na frente

protagonista_state = protagonista_frente2

# =========================================================
# Tela de Combate
# =========================================================
cenario_luta = pygame.image.load("Imagens/CenarioLuta.png").convert() # Fundinho do combate
boneco_luta = pygame.image.load("Imagens/BonecoLuta.png").convert_alpha() # Pose de Luta do personagem
luz_luta = pygame.image.load("Imagens/LuzLuta.png").convert_alpha() # Luzinha embaixo dos inimigos
# =========================================================
# Tela de Poções
# =========================================================
sprites_pocoes_de_cura = pygame.image.load("Imagens/PocoesDeCura.png").convert()
# sprites_pocoes_de_buff = pygame.image.load("Imagens/PocoesDeBuff.png").convert() Não vou botar pra entrar por agora

def get_image(sheet, tier, width, height): # pega imagem
    image = pygame.Surface((width, height), pygame.SRCALPHA) # o parâmetro pygame.SRCALPHA indica um surface com fundo transparente
    image.blit(sheet, (0,0), (tier * width, 0, width, height))
    return image
pocao_tier1 = get_image(sprites_pocoes_de_cura, 0, 24, 30)
pocao_tier2 = get_image(sprites_pocoes_de_cura, 1, 24, 30)
pocao_tier3 = get_image(sprites_pocoes_de_cura, 2, 24, 30)
pocao_tier4 = get_image(sprites_pocoes_de_cura, 3, 24, 30)
# =========================================================
# Tela de Game Over
# =========================================================
tela_gameover = pygame.image.load("Imagens/VocePerdeu.png").convert()
botao_jogarnovamente = pygame.image.load("Imagens/JogarNovamente.png").convert()
botao_sair = pygame.image.load("Imagens/Sair.png").convert()

botao_jogarnovamente_rect = botao_jogarnovamente.get_rect()
botao_jogarnovamente_rect.center = (400, 600)
botao_sair_rect = botao_sair.get_rect()
botao_sair_rect.center = (900, 600)
# =========================================================
# Monstros
# =========================================================
###### Monstros Tier 1
sprites_monstros_tier1 = pygame.image.load("Imagens/Monstros/MonstrosTier1.png")
tier1_monstro1 = pygame.transform.scale_by(get_sprite(sprites_monstros_tier1, 0, 144, 96), 1.75)
tier1_monstro2 = pygame.transform.scale_by(get_sprite(sprites_monstros_tier1, 148, 288, 96), 1.75)
tier1_monstro3 = pygame.transform.scale_by(get_sprite(sprites_monstros_tier1, 272, 399, 96), 1.75)
tier1_monstro4 = pygame.transform.scale_by(get_sprite(sprites_monstros_tier1, 416, 543, 96), 1.75)
tier1_monstro5 = pygame.transform.scale_by(get_sprite(sprites_monstros_tier1, 544, 656, 96), 1.75)
monstros_tier1 = [tier1_monstro1, tier1_monstro2, tier1_monstro3, tier1_monstro4, tier1_monstro5]
###### Monstros Tier 2
sprites_monstros_tier2 = pygame.image.load("Imagens/Monstros/MonstrosTier2.png")
tier2_monstro1 = pygame.transform.scale_by(get_sprite(sprites_monstros_tier2, 0, 144, 112), 1.6)
tier2_monstro2 = pygame.transform.scale_by(get_sprite(sprites_monstros_tier2, 145, 288, 112), 1.6)
tier2_monstro3 = pygame.transform.scale_by(get_sprite(sprites_monstros_tier2, 289, 432, 112), 1.6)
tier2_monstro4 = pygame.transform.scale_by(get_sprite(sprites_monstros_tier2, 433, 576, 112), 1.6)
tier2_monstro5 = pygame.transform.scale_by(get_sprite(sprites_monstros_tier2, 577, 719, 112), 1.6)
tier2_monstro6 = pygame.transform.scale_by(get_sprite(sprites_monstros_tier2, 720, 864, 112), 1.6)
monstros_tier2 = [tier2_monstro1, tier2_monstro2, tier2_monstro3, tier2_monstro4, tier2_monstro5, tier2_monstro6]
###### Monstros Tier 3
sprites_monstros_tier3 = pygame.image.load("Imagens/Monstros/MonstrosTier3.png")
tier3_monstro1 = pygame.transform.scale_by(get_sprite(sprites_monstros_tier3, 0, 160, 160), 1.75)
tier3_monstro2 = pygame.transform.scale_by(get_sprite(sprites_monstros_tier3, 161, 320, 160), 1.75)
tier3_monstro3 = pygame.transform.scale_by(get_sprite(sprites_monstros_tier3, 321, 496, 160), 1.75)
tier3_monstro4 = pygame.transform.scale_by(get_sprite(sprites_monstros_tier3, 497, 704, 160), 1.75)
tier3_monstro5 = pygame.transform.scale_by(get_sprite(sprites_monstros_tier3, 705, 896, 160), 1.75)
tier3_monstro6 = pygame.transform.scale_by(get_sprite(sprites_monstros_tier3, 897, 1056, 160), 1.75)
monstros_tier3 = [tier3_monstro1, tier3_monstro2, tier3_monstro3, tier3_monstro4, tier3_monstro5, tier3_monstro6]
###### Monstros Tier 4
sprites_monstros_tier4 = pygame.image.load("Imagens/Monstros/MonstroTier4.png")
tier4_monstro1 = pygame.transform.scale_by(get_sprite(sprites_monstros_tier4, 0, 256, 224), 2)
tier4_monstro2 = pygame.transform.scale_by(get_sprite(sprites_monstros_tier4, 257, 448, 224), 2)
tier4_monstro3 = pygame.transform.scale_by(get_sprite(sprites_monstros_tier4, 449, 672, 224), 2)
tier4_monstro4 = pygame.transform.scale_by(get_sprite(sprites_monstros_tier4, 673, 880, 224), 2)
tier4_monstro5 = pygame.transform.scale_by(get_sprite(sprites_monstros_tier4, 881, 1088, 224), 2)
monstros_tier4 = [tier4_monstro1, tier4_monstro2, tier4_monstro3, tier4_monstro4, tier4_monstro5]
# =========================================================
# =========================================================
# FINALIZOU A IMPORTAÇÃO DE IMAGENS
# =========================================================

# =========================================================
# Variaveis pra poder meter o mapa
# =========================================================

player_pos = pygame.Vector2(94, 5670)
velocidade = 32

camera = pygame.Rect(0, 0, 1280, 720)

sala_atual = None
primeira_sala = True

SALA_LARGURA = 288
SALA_ALTURA = 288
def get_sala_atual(pos):
    col = int(pos.x // SALA_LARGURA)
    row = int(pos.y // SALA_ALTURA)
    return row * 100 + col  # ID único

salas_visitadas = set()

blocos_na_sala = 0
chance_base_combate = 0.20
max_blocos = 5

def chance_combate():
    progresso = blocos_na_sala / max_blocos
    return min(1.0, chance_base_combate + (1.0 - chance_base_combate) * progresso)

# =========================================================
# Oq e herdado das outras runs tlgd
# =========================================================
meta = {
    "forca": 0, # TROCAR ISSO PRA 0 DEPOIS
    "destreza": 0,
    "constituicao": 0, # TROCAR ISSO PRA 0 DEPOIS
    "sorte": 0
}

ultima_heranca = meta.copy()

# =========================================================
# Upar de level
# =========================================================
level_up_options = ["FORÇA", "DESTREZA", "CONSTITUIÇÃO", "SORTE"]
opcao_level_up = 0

STAT_MAP = {
    "FORÇA": "forca",
    "DESTREZA": "destreza",
    "CONSTITUIÇÃO": "constituicao",
    "SORTE": "sorte"
}

# =========================================================
# Jogador ai
# =========================================================
def nova_run():
    base = 5
    return {
        "hp": 0,
        "max_hp": 0,

        "base_forca": base,
        "base_destreza": base,
        "base_constituicao": base,
        "base_sorte": base,

        "start_forca": base,
        "start_destreza": base,
        "start_constituicao": base,
        "start_sorte": base,

        "forca": base + meta["forca"],
        "destreza": base + meta["destreza"],
        "constituicao": base + meta["constituicao"],
        "sorte": base + meta["sorte"],

        "level": 1,
        "exp": 0,
        "exp_next": 20,
        "pontos": 0,
        "sala": 0,

        "pocoes": {
            "simples": 0,
            "media": 0,
            "avancada": 0,
            "especial": 0
        }
    }

player = nova_run()
inimigo = {}
critico_ativo = False

# =========================================================
# Vida
# =========================================================
def recalcular_vida(old_max=None): # mlk q giro foi esse q precisa dar pra poder atualizar uma variavel pqp nao aguento mais
    new_max = 10 + player["constituicao"] * 2

    if old_max is None:
        player["hp"] = new_max
    else:
        player["hp"] += new_max - old_max

    player["max_hp"] = new_max
    player["hp"] = min(player["hp"], player["max_hp"])

recalcular_vida()

# =========================================================
# Inimigos
# =========================================================

def get_tier(sala): # define o tier
    if sala <= 25:
        return 1
    elif sala <= 50:
        return 2
    elif sala <= 75:
        return 3
    else:
        return 4

def exp_por_tier(tier): # define o xp pelo tier ne pit
    return {1: 20, 2: 40, 3: 80, 4: 160}[tier] # 20 40 80 160

def criar_inimigo(sala): # cria os status dele memo
    tier = get_tier(sala)
    return {
        "hp": 12 + sala * 2,
        "dano": 2 + sala,
        "tier": tier,
        "exp": exp_por_tier(tier)
    }

def escolher_sprite_inimigo(tier):
    if tier == 1:
        return random.choice([
            tier1_monstro1, tier1_monstro2, tier1_monstro3,
            tier1_monstro4, tier1_monstro5
        ])
    elif tier == 2:
        return random.choice([
            tier2_monstro1, tier2_monstro2, tier2_monstro3,
            tier2_monstro4, tier2_monstro5, tier2_monstro6
        ])
    elif tier == 3:
        return random.choice([
            tier3_monstro1, tier3_monstro2, tier3_monstro3,
            tier3_monstro4, tier3_monstro5, tier3_monstro6
        ])
    else:
        return random.choice([
            tier4_monstro1, tier4_monstro2, tier4_monstro3,
            tier4_monstro4, tier4_monstro5
        ])
# =========================================================
# Combate
# =========================================================
acabou_combate = False

def calcular_dano_jogador():
    global critico_ativo
    critico_ativo = False

    base = player["forca"] + player["destreza"] * 0.5
    crit_chance = 0.05 + player["sorte"] * 0.005
    bonus_crit = player["forca"] * 0.6

    if random.random() < crit_chance:
        critico_ativo = True
        return int(base + bonus_crit)

    return int(base)

def calcular_dano_recebido(dano_base): # Defesa games
    """
    Reduz o dano recebido com base na CONSTITUIÇÃO.
    Existe um cap pra não virar imortal
    """
    reducao = player["constituicao"] * 0.006  # 0.6% por ponto
    reducao = min(reducao, 0.60)              # cap de 60%

    dano_final = int(dano_base * (1 - reducao))
    return max(1, dano_final)                 # nunca toma 0

def chance_fuga():
    chance = 0.2 + player["destreza"] * 0.005 + player["sorte"] * 0.015
    return min(0.95, chance)

# =========================================================
# Pocao ai slk
# =========================================================
cura_pocao = {
    "simples": 0.25,
    "media": 0.45,
    "avancada": 0.7,
    "especial": 1.0
}

POTION_MAP = {
    "SIMPLES": "simples",
    "MÉDIA": "media",
    "AVANÇADA": "avancada",
    "ESPECIAL": "especial"
}

def dropar_pocao(tier):
    """
    Sorte influencia:
    - quantidade de rolagens
    - chance de poções melhores
    - nenhuma chance chega a 100%
    """
    # quantidade de rolls com sorte
    rolls = 1 + player["sorte"] // 20

    for _ in range(rolls):
        luck = player["sorte"] * 0.003
        roll = random.random()

        # Ajuste de qualidade baseado no tier + sorte
        if tier == 1:
            if roll < 0.35 + luck:
                player["pocoes"]["simples"] += 1
            elif roll < 0.42 + luck * 0.6:
                player["pocoes"]["media"] += 1

        elif tier == 2:
            if roll < 0.30 + luck:
                player["pocoes"]["media"] += 1
            elif roll < 0.38 + luck * 0.6:
                player["pocoes"]["avancada"] += 1

        elif tier == 3:
            if roll < 0.28 + luck:
                player["pocoes"]["avancada"] += 1
            elif roll < 0.35 + luck * 0.5:
                player["pocoes"]["especial"] += 1

        elif tier == 4:
            if roll < 0.30 + luck * 0.8:
                player["pocoes"]["especial"] += 1

def usar_pocao(tipo):
    if player["pocoes"][tipo] > 0:
        cura = int(player["max_hp"] * cura_pocao[tipo])
        player["hp"] = min(player["hp"] + cura, player["max_hp"])
        player["pocoes"][tipo] -= 1
        return True
    return False

# =========================================================
# Pegar os status da run antiga ai
# =========================================================
def aplicar_heranca():
    global ultima_heranca
    ultima_heranca = {
        "forca": math.floor((player["base_forca"] - player["start_forca"]) * 0.8),
        "destreza": math.floor((player["base_destreza"] - player["start_destreza"]) * 0.8),
        "constituicao": math.floor((player["base_constituicao"] - player["start_constituicao"]) * 0.8),
        "sorte": math.floor((player["base_sorte"] - player["start_sorte"]) * 0.8),
    }
    for s in meta:
        meta[s] += max(0, ultima_heranca[s])

def atualizar_status_finais():
    for s in meta:
        player[s] = player[f"base_{s}"] + meta[s]

# =========================================================
# Aumentar +1 em cada atributinho ai
# =========================================================
def bonus_global_level(old_max):
    if player["level"] % 3 == 0:
        for s in ["forca", "destreza", "constituicao", "sorte"]:
            player[f"base_{s}"] += 1
        atualizar_status_finais()
        recalcular_vida(old_max)

# =========================================================
# Desenho
# =========================================================
def draw_text(text, x, y, selected=False):
    color = (255, 255, 0) if selected else (255, 255, 255)
    if selected == True:
        screen.blit(setinha, (x-32, y+4))
    screen.blit(font.render(text, True, color), (x, y))

# =========================================================
# Menuzinhos
# =========================================================
combat_options = ["ATACAR", "POÇÃO", "FUGIR"]
opcao_combate = 0

potion_menu_options = ["ESPECIAL", "AVANÇADA", "MÉDIA", "SIMPLES", "VOLTAR"]
imagens_menu_pocoes = [pocao_tier4, pocao_tier3, pocao_tier2, pocao_tier1]
opcao_pocao = 0

# =========================================================
# Jogo memo ai
# =========================================================

# variavel pra porra nenhuma ta
def sair():
    pygame.quit()
    sys.exit()
# acho q foi mascena q usou e eu achei bonito entao copiei
sprite_inimigo_atual = None
running = True
tick_andar = 0
while running:
    clock.tick(90)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair()

        # Esse resto aq é jogo
        if event.type == pygame.KEYDOWN:
            if state == STATE_TITLE:
                if event.key == pygame.K_RETURN:
                    state = STATE_DUNGEON
                    inicio = True
            
            if event.key == pygame.K_ESCAPE and state == STATE_POTION_MENU:
                state = STATE_COMBAT

            elif state == STATE_COMBAT:
                if event.key == pygame.K_UP:
                    opcao_combate = (opcao_combate - 1) % len(combat_options)
                elif event.key == pygame.K_DOWN:
                    opcao_combate = (opcao_combate + 1) % len(combat_options)

                elif event.key == pygame.K_RETURN:
                    escolha = combat_options[opcao_combate]

                    if escolha == "ATACAR":
                        inimigo["hp"] -= calcular_dano_jogador()
                        if inimigo["hp"] > 0:
                            player["hp"] -= calcular_dano_recebido(inimigo["dano"])

                    elif escolha == "FUGIR":
                        if random.random() < chance_fuga():
                            # Cura 55% da VIDA ATUAL
                            cura = int(player["max_hp"] * 0.35)
                            player["hp"] = min(player["hp"] + cura, player["max_hp"])
                            acabou_combate = True
                            state = STATE_DUNGEON
                            continue
                        else:
                            player["hp"] -= calcular_dano_recebido(inimigo["dano"])

                    elif escolha == "POÇÃO":
                        opcao_pocao = 0
                        state = STATE_POTION_MENU
                        continue

                    if player["hp"] <= 0:
                        aplicar_heranca()
                        state = STATE_GAMEOVER
                        continue

                    if inimigo["hp"] <= 0:
                        dropar_pocao(inimigo["tier"])
                        player["exp"] += inimigo["exp"]
                        acabou_combate = True
                        while player["exp"] >= player["exp_next"]:
                            old = player["max_hp"]
                            player["exp"] -= player["exp_next"]
                            player["level"] += 1
                            player["exp_next"] = player["level"] * 20
                            player["pontos"] += 7
                            bonus_global_level(old)
                            opcao_level_up = 0
                            state = STATE_LEVEL_UP
                            break
                        else:
                            state = STATE_DUNGEON

            elif state == STATE_POTION_MENU:
                if event.key == pygame.K_UP:
                    opcao_pocao = (opcao_pocao - 1) % len(potion_menu_options)
                elif event.key == pygame.K_DOWN:
                    opcao_pocao = (opcao_pocao + 1) % len(potion_menu_options)

                elif event.key == pygame.K_RETURN:
                    opt = potion_menu_options[opcao_pocao]
                    if opt == "VOLTAR":
                        state = STATE_COMBAT
                    else:
                        tipo = POTION_MAP[opt]
                        if not usar_pocao(tipo):
                            player["hp"] -= calcular_dano_recebido(inimigo["dano"])
                        state = STATE_COMBAT

            elif state == STATE_LEVEL_UP:
                if event.key == pygame.K_UP:
                    opcao_level_up = (opcao_level_up - 1) % len(level_up_options)
                elif event.key == pygame.K_DOWN:
                    opcao_level_up = (opcao_level_up + 1) % len(level_up_options)

                elif event.key == pygame.K_RETURN and player["pontos"] > 0:
                    old = player["max_hp"]
                    stat = STAT_MAP[level_up_options[opcao_level_up]]
                    player[f"base_{stat}"] += 1
                    player["pontos"] -= 1
                    atualizar_status_finais()
                    recalcular_vida(old)

                    if player["pontos"] <= 0:
                        state = STATE_DUNGEON

            elif state == STATE_GAMEOVER and event.key == pygame.K_r:
                player = nova_run()
                player_pos = pygame.Vector2(94, 5670)
                atualizar_status_finais()
                recalcular_vida()
                inimigo = {}
                state = STATE_DUNGEON

            elif state == STATE_GAMEOVER and event.key == pygame.K_ESCAPE:
                sair()

    # =========================
    # EXPLORAÇÃO
    # =========================
    if tick_andar%14 == 0:
        keys = pygame.key.get_pressed()
        if state == STATE_DUNGEON:
            nova_pos = player_pos.copy()
            if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                if keys[pygame.K_LEFT]:
                    nova_pos.x -= velocidade
                    state_jogador = 'esquerda'
                if keys[pygame.K_RIGHT]:
                    nova_pos.x += velocidade
                    state_jogador = 'direita'
            elif keys[pygame.K_UP] or keys[pygame.K_DOWN]:
                if keys[pygame.K_UP]:
                    nova_pos.y -= velocidade
                    state_jogador = 'frente'
                if keys[pygame.K_DOWN]:
                    nova_pos.y += velocidade
                    state_jogador = 'baixo'

            ajuste_hitbox = pygame.Vector2(16,48)

            colisao = nova_pos + ajuste_hitbox
            if pode_andar(colisao):
                player_pos = nova_pos

                if not acabou_combate:
                    blocos_na_sala = min(blocos_na_sala + 1, max_blocos)

                    if random.random() < chance_combate():
                        player["sala"] += 1
                        inimigo = criar_inimigo(player["sala"])
                        sprite_inimigo_atual = escolher_sprite_inimigo(inimigo["tier"])
                        opcao_combate = 0
                        critico_ativo = False
                        acabou_combate = True
                        state = STATE_COMBAT


            if state_jogador == 'baixo':
                protagonista_state = protagonista_baixo2
            elif state_jogador == 'esquerda':
                protagonista_state = protagonista_lado2
            elif state_jogador == 'direita':
                protagonista_state = pygame.transform.flip(protagonista_lado2, True, False)
            elif state_jogador == 'frente':
                protagonista_state = protagonista_frente2
    tick_andar += 1 

    # Entrar em combate se bater de cara com uma sala
    if state == STATE_DUNGEON:
        nova_sala = get_sala_atual(player_pos)

        player_rect = pygame.Rect(player_pos.x, player_pos.y, 32, 64)
        map_rect = todas_salas.get_rect()

        if player_rect.left < map_rect.left:
            player_pos.x = map_rect.left
        if player_rect.right > map_rect.right:
            player_pos.x = map_rect.right - player_rect.width
        if player_rect.top < map_rect.top:
            player_pos.y = map_rect.top
        if player_rect.bottom > map_rect.bottom:
            player_pos.y = map_rect.bottom - player_rect.height
            
        if sala_atual is None:
            sala_atual = nova_sala
            salas_visitadas.add(nova_sala)
            blocos_na_sala = 0
            primeira_sala = False

        elif nova_sala != sala_atual:
            sala_atual = nova_sala
            blocos_na_sala = 0
            acabou_combate = False

            if nova_sala not in salas_visitadas:
                salas_visitadas.add(nova_sala)





    # =========================
    # CÂMERA
    # =========================
    camera.center = player_pos
    # Limites do mapa
    camera.clamp_ip(todas_salas.get_rect())

    # =====================================================
    # Desenhos
    # =====================================================
    screen.fill((0, 0, 0))

    if state == STATE_TITLE:
        # Fundo
        screen.blit(title_bg, (0, 0))

        # Botão
        screen.blit(botao_jogar, botao_rect)

        # Texto acima do botão
        texto = font.render("Pressione ENTER para Jogar", True, (0, 0, 0))
        texto_rect = texto.get_rect()
        texto_rect.center = (930, botao_rect.top - 30)
        screen.blit(texto, texto_rect)

    if state == STATE_DUNGEON:
        # Mapa (recortado pela câmera)
        screen.blit(todas_salas, (0, 0), camera)
        # Player (posição relativa à câmera)
        screen.blit(protagonista_state,(player_pos.x - camera.x, player_pos.y - camera.y))
        # HUD
        draw_text(f"SALA: {player['sala']}", 40, 40)
        draw_text(f"LEVEL: {player['level']}", 40, 70)
        draw_text(f"HP: {player['hp']} / {player['max_hp']}", 40, 100)

    elif state == STATE_COMBAT:
        screen.blit(cenario_luta, (0, 0))

        # Inimigo
        screen.blit(luz_luta, (0, 0))
        if sprite_inimigo_atual in monstros_tier1:
            screen.blit(sprite_inimigo_atual, (810-40, 210-30))
        elif sprite_inimigo_atual in monstros_tier2:
            screen.blit(sprite_inimigo_atual, (780-60, 210-40))
        elif sprite_inimigo_atual in monstros_tier3:
            screen.blit(sprite_inimigo_atual, (780-70, 170-60))
        elif sprite_inimigo_atual in monstros_tier4:
            screen.blit(sprite_inimigo_atual, (760-100, 140-80))

        # Jogador
        screen.blit(boneco_luta, (0, 0))

        # HUD
        draw_text(f"HP: {player['hp']} / {player['max_hp']}", 40, 580)
        draw_text(f"Inimigo HP: {inimigo['hp']}", 40, 620)

        for i, opt in enumerate(combat_options):
            draw_text(opt, 300, 550 + i * 48, selected=(i == opcao_combate))
#312 428
    elif state == STATE_POTION_MENU:
        draw_text("POÇÕES", 40, 40)
        for i, opt in enumerate(potion_menu_options):
            if opt == "VOLTAR":
                texto = "VOLTAR"
            else:
                chave = POTION_MAP[opt]
                texto = f"     {opt} ({player['pocoes'][chave]})"
            screen.blit(pocao_tier4, (96, 118))
            screen.blit(pocao_tier3, (96, 158))
            screen.blit(pocao_tier2, (96, 198))
            screen.blit(pocao_tier1, (96, 238))
            draw_text(texto, 100, 120 + i * 40, selected=(i == opcao_pocao))

    elif state == STATE_LEVEL_UP:
        draw_text("LEVEL UP!", 40, 40)
        draw_text(f"Pontos restantes: {player['pontos']}", 40, 80)
        for i, opt in enumerate(level_up_options):
            draw_text(opt, 40, 140 + i * 40, selected=(i == opcao_level_up))

    elif state == STATE_GAMEOVER:
        screen.blit(tela_gameover, (0, 0))

        draw_text("Para jogar novamente \naperte a tecla R", 205, 446)
        screen.blit(botao_jogarnovamente, botao_jogarnovamente_rect)
        draw_text("Para sair \naperte a tecla ESC", 705, 446)
        screen.blit(botao_sair, botao_sair_rect)

        # # Texto acima do botão
        # texto = font.render("Pressione ENTER para Jogar", True, (0, 0, 0))
        # texto_rect = texto.get_rect()
        # texto_rect.center = (930, botao_rect.top - 30)
        # screen.blit(texto, texto_rect)


    pygame.display.flip()