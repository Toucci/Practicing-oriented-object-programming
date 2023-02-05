#criando uma classe herança
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        # definindo que os likes começam em 0
        self._likes = 0

        # definindo uma propriedade para o método likes, onde ele retorna o valor de self.__likes
        # Quando um atributo é privado, onde ele for chamado dará erro(como nos prints que chamam o número de likes)
        # Ao criar esse property, podemos retornar o valor de self._likes que encontra-se privado

    @property
    def likes(self):
        return self._likes

    # método para os likes para cada filme
    def dar_Like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    # Serve para inserir valor dentro do nome
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes'


#Criando a classe(entidade forte) filme, com seus respectivos atributos
class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao}min - {self._likes} Likes'

#Criando a classe(entidade forte) série, com seus respectivos atributos
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        #super init serve para chamar a programação do nome e ano diretamente da classe mãe
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} Temporadas - {self._likes} Likes'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    #método que diz que uma classe pode ter iterável
    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)



#colocando os dados do filme
vingadores = Filme('vingadores: ultimato', 2019, '3h2')
#colocando os dados da série
atlanta = Serie('atlanta', 2017, 2)

tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)
tmoc = Serie('todo mundo odeia o chris', 2012, 5)


#Dando um like no filme
vingadores.dar_Like()
tmoc.dar_Like()
tmoc.dar_Like()
tmoc.dar_Like()
tmep.dar_Like()
tmep.dar_Like()
tmep.dar_Like()
tmep.dar_Like()
demolidor.dar_Like()
demolidor.dar_Like()
#Dando três likes para a série Atlanta
atlanta.dar_Like()
atlanta.dar_Like()
atlanta.dar_Like()

#criando a playlist
filmes_e_series = [vingadores, atlanta, demolidor, tmep, tmoc]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)


print(f'Tamanho da Playlist: {len(playlist_fim_de_semana)}')
#este for percorre os programas que estão dentro da playlist
for programa in playlist_fim_de_semana:
    print(programa)

print(playlist_fim_de_semana[0])


#verificando se um filme ou série está na playlist
print(f'Tá ou não tá? {tmoc in playlist_fim_de_semana}')