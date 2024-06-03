import os
import json
# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

def listar(tarefas):
    if not tarefas:
        print('Nenhuma tarefa a ser listada')
        print('')
        return    
    print('Tarefas: ') 
    print(*tarefas, sep='\n')
    print('')

def desfazer(tarefas, tarefas_refazer):
    print('')
    if not tarefas:
        print('Nenhuma tarefa a desfazer')
        print('')
        return
    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)
    print(f'{tarefa=} foi removida')
    listar(tarefas)
    print('')

def refazer(tarefas, tarefas_refazer):
    print('')
    if not tarefas_refazer:
        print('Nenhuma tarefa a refazer')
        print('')
        return
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)
    print(f'{tarefa=} foi removida')
    listar(tarefas)
    print('')

def adcionar(tarefa, tarefas):
    print('')
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa')
        print('')
        return
    tarefas.append(tarefa)
    listar(tarefas)
    print('')

def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        salvar(tarefas, caminho_arquivo)
    return dados

def salvar(tarefas, caminho_arquivo):
        with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
            json.dump(
                tarefas,
                arquivo,
                indent=2,
                ensure_ascii=False
            )
        return

CAMINHO_ARQUIVO = 'D:\\Carlos\\Estudos Pessoais\\python\\curso_python\\Intermediario\\aula119_ExerciseBD.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer, refazer')
    user = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('cls'),
        'adicionar': lambda: adcionar(user, tarefas),
    }

    comando = comandos.get(user) if comandos.get(user) is not None else \
        comandos['adicionar']
    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)


    # if user == 'listar':
    #     listar(tarefas)
    #     continue

    # elif user == 'desfazer':
    #     desfazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
    #     continue

    # elif user == 'refazer':
    #     refazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
    #     continue
    # elif user == 'clear':
    #     os.system('cls')
    #     continue
    # else:
    #     adcionar(user.title(), tarefas)
    #     listar(tarefas)
    #     continue
