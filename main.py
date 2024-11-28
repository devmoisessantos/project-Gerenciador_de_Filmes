from filmes import Filme
from menu import * 

filmes = {}  # Dicionário para armazenar os filmes

while True:
    limpar_tela()
    menu_principal()
    escolha = input('>>> ')

    if not escolha.isdigit():
        limpar_tela()
        print('Digite uma opção válida.')
        sleep(1)
        continue
    
    escolha = int(escolha)

    if escolha == 1:
        limpar_tela()
        print('Adicionar um novo filme:\n')
        nome_do_filme = input('Digite o nome do filme: ')
        ano_lancamento = int(input('Digite o ano de lançamento: '))
        nota_imdb = float(input('Digite a nota do IMDB: '))
        incluido_em = input('Incluído em: ')
        duracao = input('Duração: ')

        filme = Filme(nome_do_filme, ano_lancamento, nota_imdb, incluido_em, duracao)
        filmes[nome_do_filme] = filme
        limpar_tela()
        print(f'O filme "{nome_do_filme}" foi adicionado com sucesso!\n')

    elif escolha == 2:
        limpar_tela()
        if not filmes:
            print("Nenhum filme foi adicionado ainda.\n")
        else:
            print('Escolha um filme para avaliar:\n')
            for nome in filmes:
                print(f'- {nome}')
            nome_filme = input('\nDigite o nome do filme para avaliar ou "sair" para voltar: ')

            if nome_filme == 'sair':
                continue
            elif nome_filme in filmes:
                filme = filmes[nome_filme]
                while True:
                    menu_avaliar(filme)
                    nota = input('>>> ')
                    if nota == 'sair':
                        break
                    try:
                        nota = float(nota)
                        filme.avaliar_filme(nota)
                    except ValueError:
                        print('Nota inválida. Digite um número válido entre 0 e 10.')
                        sleep(1)
                        continue
            else:
                print('Filme não encontrado. Tente novamente.\n')
                sleep(1)

    elif escolha == 3:
        limpar_tela()
        if not filmes:
            print("Nenhum filme foi adicionado ainda.\n")
        else:
            print('Escolha um filme para ver a média das avaliações:\n')
            for nome in filmes:
                print(f'- {nome}')
            nome_filme = input('\nDigite o nome do filme para ver a média ou "sair" para voltar: ')

            if nome_filme == 'sair':
                continue
            elif nome_filme in filmes:
                filme = filmes[nome_filme]
                filme.calcular_media()
            else:
                print('Filme não encontrado. Tente novamente.\n')
                sleep(1)

    elif escolha == 4:
        limpar_tela()
        if not filmes:
            print("Nenhum filme foi adicionado ainda.\n")
        else:
            print('Lista de filmes:\n')
            for nome, filme in filmes.items():
                print(f'Nome: {filme.nome}, Ano: {filme.ano_lancamento}, Duração: {filme.duracao}')
        input('\nPressione Enter para voltar ao menu principal.')

    elif escolha == 5:
        limpar_tela()
        sair_do_programa()

    else:
        limpar_tela()
        print('Opção inválida. Tente novamente.')
        sleep(1)

if __name__ == '__main__':
    main()