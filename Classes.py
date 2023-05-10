"""
CLASSE = PESSOA
   MÉTODO = ANDAR, PULAR, CORRER ETC (O QUE FAZ)
   ATRIBUTOS = PESO, ALTURA, COR ETC (INFORMAÇÕES)

CLASSE = TV
   MÉTODO = LIGAR TV, MUDAR CANAL, VOLUME ETC
   ATRIBUTOS = COR, TAMANHO, É OU NÃO SMART TV

CLASSE = STRING 
    MÉTODO = REPLACE, FIND, CAPITALIZE, FORMAT

CLASSE = pandas.DataFrame
    MÉTODO = append, copy, dropna, groupby,filter.
    ATRIBUTOS = ILOC, COLUMNS, VALUES ETC
"""
"""
Sempre que criamos uma classe vamos precisar de:

class nome_classe:
Dentro da classe vamos criar funções(métodos) __init__ 
Esse método é quem define o que acopntece quando você cria uma instancia da classe
self é um parametro que identifica atributos de uma classe.
"""
class TV():

    def __init__(self):
        self.cor = "preta" # self.cor (atributo) preta(variavel qualquer)
        self.tamanho = 55
        self.canal = 10
        self.volume = 50
        self.canal = "netflix"
    
    def mudar_canal(self, novo_canal):
        self.canal = novo_canal




tv_sala = TV()
tv_quarto = TV()

tv_sala.mudar_canal("globo")
print(tv_sala.canal)



