
from os import system
from time import sleep
from filmes import Filme

def limpar_tela():
    system('cls') 


def menu_principal():
    print(
        'Avaliador de Filmes:\n\n'
        '1. Adicionar filme\n'
        '2. Avaliar filme\n'
        '3. Ver média de avaliações\n'
        '4. Listar filmes\n'
        '5. Sair\n\n'
        'Digite a opção desejada: '
    )


def menu_avaliar(filme: str):

    print(
        f'Avaliador de Filmes - {filme}\n\n'
        'Digite a nota do filme (0-10) ou "sair" para voltar: '
    )


def sair_do_programa():
    print("Saindo do programa...")
    sleep(1)
    exit()

menu = menu_avaliar('Avatar')
print(menu)