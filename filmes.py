class Filme:
    def __init__(self, nome, ano_lancamento, nota_imdb, incluido_em, duracao):
        self.nome = nome
        self.total_notas = 0
        self.total_avaliadores = 0
        self.ano_lancamento = ano_lancamento
        self.nota_imdb = nota_imdb
        self.incluido_em = incluido_em
        self.duracao = duracao
    
    def __str__(self):
        return f'{self.nome}'
    
    def ficha_tecnica(self):
        print(
            'Ficha Técnica\n'
            '-------------\n'
            'Dados do Filme:\n\n'
            f'Nome: {self.nome}\n'
            f'Ano de Lançamento: {self.ano_lancamento}\n'
            f'Nota IMDB: {self.nota_imdb}\n'
            f'Incluído em: {self.incluido_em}\n'
            f'Duração: {self.duracao}\n'
        )
    
    def avaliar_filme(self, nota: float):
        if \
            nota < 0 or nota > 10:
            print(
                f'Nota "{nota}" inválida... Insira uma nota entre 0 e 10.'
            )
        else:
            self.total_notas += nota
            self.total_avaliadores += 1
            print(
                f'\nSua nota para "{self.nome}" foi registrada com sucesso.'
                f'Avaliadores: {self.total_avaliadores}'
            )
    
    def calcular_media(self):
        if \
            self.total_avaliadores == 0:
            print(f'Filme: {self.nome}\n'
                  'Ainda não houve avaliações.\n'
            )
                  
        else:
            media = self.total_notas / self.total_avaliadores
            print(f'Filme: {self.nome}\nNota Média: {media:.1f}\n')
