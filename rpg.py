import random
import json

# Arquivo para salvar o progresso
ARQUIVO_SALVAMENTO = "progresso_rpg.json"

# Função para carregar o progresso
def carregar_progresso():
    try:
        with open(ARQUIVO_SALVAMENTO, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return None

# Função para salvar o progresso
def salvar_progresso():
    with open(ARQUIVO_SALVAMENTO, "w") as arquivo:
        json.dump(player, arquivo, indent=4)

# Função para resetar o progresso
def resetar_progresso():
    global player
    nickname = input("\nInsira um novo nome para recomeçar sua jornada: ")
    level = 1
    player = {
        'nickname': nickname,
        'level': level,
        'level_max': 50,
        'exp': 0,
        'exp_max': 50,
        'hp': 100 * level,
        'hp_max': 100 * level,
        'dano': 25 * level,
    }
    salvar_progresso()
    print(f"\nA jornada foi resetada! Bem-vindo, {player['nickname']}.")

# Boas-vindas
print('Bem-vindo ao RPG Python!')
print('Aqui você poderá se divertir com um simples jogo de RPG!')

# Player
dados_carregados = carregar_progresso()
if dados_carregados:
    print("\nProgresso carregado com sucesso!")
    player = dados_carregados
else:
    nickname = input('Insira seu nome (não use seu nome real): ')
    level = 1
    player = {
        'nickname': nickname,
        'level': level,
        'level_max': 50,
        'exp': 0,
        'exp_max': 50,
        'hp': 100 * level,
        'hp_max': 100 * level,
        'dano': 25 * level,
    }

def mostrar_estatísticas():
    print("\n--- Suas estatísticas ---")
    print(f"Nome: {player['nickname']}")
    print(f"Level: {player['level']}")
    print(f"EXP: {player['exp']}/{player['exp_max']}")
    print(f"HP: {player['hp']}/{player['hp_max']}")
    print(f"Dano: {player['dano']}")

def level_up():
    if player['exp'] >= player['exp_max']:
        player['level'] += 1
        player['exp'] = 0
        player['exp_max'] *= 2
        player['hp_max'] = int(player['hp_max'] * 1.75)
        player['hp'] = player['hp_max']  # Restaura HP ao máximo
        player['dano'] *= 2
        print(f"\nParabéns! {player['nickname']} subiu para o nível {player['level']}!")
        salvar_progresso()

# Gerando monstros
def gerar_monstro():
    level = random.randint(1, 25)
    npc_gerado = {
        'nome': f"Monstro #{level}",
        'level': level,
        'exp': 7 * level,
        'hp': 100 * level,
        'hp_max': 100 * level,
        'dano': 5 * level,
    }
    return npc_gerado

# Batalha
def batalha():
    npc = gerar_monstro()
    print("\n--- Iniciando batalha! ---")
    print(f"Player: {player['nickname']} // Level: {player['level']} // HP: {player['hp']}/{player['hp_max']} // Dano: {player['dano']}")
    print(f"NPC: {npc['nome']} // Level: {npc['level']} // HP: {npc['hp']}/{npc['hp_max']} // Dano: {npc['dano']}")

    while npc['hp'] > 0 and player['hp'] > 0:
        atacar_npc(npc)
        if npc['hp'] <= 0:
            player['exp'] += npc['exp']
            print(f"{player['nickname']} venceu e ganhou {npc['exp']} de EXP!")
            if player['exp'] >= player['exp_max']:
                level_up()
            salvar_progresso()
            break

        atacar_player(npc)
        if player['hp'] <= 0:
            print(f"{player['nickname']}, você foi derrotado! Seu HP foi restaurado.")
            player['hp'] = player['hp_max']
            salvar_progresso()
            break

        info_batalha(npc)

# Ataques
def atacar_npc(npc):
    npc['hp'] -= player['dano']
    print(f"{player['nickname']} atacou {npc['nome']} causando {player['dano']} de dano!")

def atacar_player(npc):
    player['hp'] -= npc['dano']
    print(f"{npc['nome']} atacou {player['nickname']} causando {npc['dano']} de dano!")

def info_batalha(npc):
    print(f"\n--- Status da batalha ---")
    print(f"Player: {player['nickname']} // HP: {player['hp']}/{player['hp_max']}")
    print(f"NPC: {npc['nome']} // HP: {npc['hp']}/{npc['hp_max']}")

# Interface do menu
def interface():
    while True:
        print("\n--- Menu ---")
        print("1 - Batalhar")
        print("2 - Estatísticas")
        print("3 - Resetar Jornada")
        print("4 - Sair")

        escolha_interface = input(f"Olá {player['nickname']}, escolha uma das opções acima: ").strip().lower()

        if escolha_interface in ['1', 'um']:
            batalha()
        elif escolha_interface in ['2', 'dois']:
            mostrar_estatísticas()
        elif escolha_interface in ['3', 'tres', 'três']:
            confirmar = input("Você tem certeza que deseja resetar sua jornada? (s/n): ").strip().lower()
            if confirmar in ['s', 'sim']:
                resetar_progresso()
        elif escolha_interface in ['4', 'quatro']:
            print("Progresso salvo. Obrigado por jogar! ❤️")
            salvar_progresso()
            break
        else:
            print("Erro! Opção inválida, tente novamente.")

# Iniciar o jogo
interface()
