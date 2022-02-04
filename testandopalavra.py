import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
p = ('eai lex bora ouvir play')
palavras_separadas = nltk.word_tokenize(p)
print(palavras_separadas)
print(p)

palavraschave = ["social", "insta", "mensagem", 4,5,6,7,8,9,10,11,12,13,14,15, "playlist", "play",
  "som", "dj", "escutar", "ouvir",21,22,23,24,25,26,27,28,29,30,31,32,333,34,35]
print(palavraschave.index("ouvir"))
tokens_musica = {"playlist" : 1, "pausar" : 2, "tocar" : 3, "pular" : 4, "volume" : 5, "pausa" : 2, "altura" : 5, "toca" : 3, "play": 3, "continua" : 6, "prosseguir" : 6}
print(tokens_musica.get('volume'))

dic_funcoes = [0, 1, pause(), play(), 4, escolher_volume(), resume()]
class interprete:
    def interpretar_texto(self):
        self.n1 = []
        for palavra in palavraschave:
            if palavra in self:
                self.n1.append(palavraschave.index(palavra))
            else:
                pass
        return n1

    def interpretar_modulo(self):
        self.modulo = []
        for i in self:
            if self.n1[i] > 0 and self.n1[i] < 10:
                self.modulo.append(tokens_social)
            elif self.n1[1] > 11  and  self.n1[i]< 25:
                self.modulo.append(tokens_musica)
        return self.modulo

    def interpretar_modulo2(self, modulo):
        

    def interpretar_atividade(self, palavras_ditas, lista_tokens):
        self.n2 = []
        self.n3 = []
        for palavra_chave in palavras_ditas:
            if palavra_chave in lista_tokens:
                self.n2.append(lista_tokens.get(palavrachave))
            else:
                self.n3.append(lista_tokens.get(palavrachave))
        return self.n2, self.n3

def selecionar_atividade(funcoes):
    atividades_lista = []
    lista_tokens_atividade = funcoes(1)
    numero = len(lista_tokens_atividade)
    for i in range(numero):
        atividades_lista.append(dic_funcoes[(lista_tokens_atividade[i])])

    return atividades_lista








interprete.interpretar(p)
