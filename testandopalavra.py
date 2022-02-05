import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
p = ('eai lex bora ouvir play')
u = nltk.word_tokenize(p)
print(u)
print(p)
print("20 16")
palavraschave = ["social", "insta", "mensagem", 4,5,6,7,8,9,10,11,12,13,14,15, "playlist", "play",
  "som", "dj", "escutar", "ouvir",21,22,23,24,25,26,27,28,29,30,31,32,333,34,35]
print(palavraschave.index("ouvir"))
tokens_musica = {"playlist" : 1, "pausar" : 2, "tocar" : 3, "pular" : 4, "aumentar" : 5 , "volume" : 5, "pausa" : 2, "altura" : 5, "toca" : 3, "play": 3, "continua" : 6, "prosseguir" : 6}
print(tokens_musica.get('volume'))

dic_funcoes = ["0, 1, pause(), play(), 4, escolher_volume(), resume()", "23, 23", "dgds", "mana", "melao"]
class interprete:
    def interpretar_texto(self):
        n1 = []
        n1_1 = []
        for palavra in self:
            if palavra in palavraschave:
                n1_1.append(palavra)
                n1.append(palavraschave.index(palavra))
            else:
                pass
        return (n1)

    def interpretar_texto2(self):
        n1 = []
        n1_1 = []
        for palavra in self:
            if palavra in palavraschave:
                n1_1.append(palavra)
                n1.append(palavraschave.index(palavra))
            else:
                pass
        return (n1_1)



    def interpretar_modulo(self):
        modulo = []
        for i in self:
            if i > 0 and i < 10:
                modulo.append(tokens_social)
            elif i > 11  and  i < 25:
                modulo.append(tokens_musica)
                break
        return (modulo[0])

    def interpretar_modulo2(self, modulo):
        pass

    def interpretar_atividade(self, palavras_ditas, lista_tokens):
        n2 = []
        n3 = []
        for palavra_chave in palavras_ditas:
            if palavra_chave in lista_tokens:
                n2.append(lista_tokens.get(str(palavra_chave)))
                print("7")
            else:
                n3.append(lista_tokens.get(palavra_chave))
        return (n2)

def selecionar_atividade(funcoes):
    atividades_lista = []
    lista_tokens_atividade = funcoes
    numero = len(lista_tokens_atividade)
    for i in range(numero):
        atividades_lista.append(dic_funcoes[(lista_tokens_atividade[i])])

    return (atividades_lista)






