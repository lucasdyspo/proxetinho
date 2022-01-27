import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
# nltk.word_tokenize
p = ('eai lex bora ouvir play')
print(p)

palavraschave = ["social", "insta", "mensagem", "playlist", "play",
  "som", "dj", "escutar", "ouvir"]
tokens_musica = {"playlist" : 1, "pausar" : 2, "tocar" : 3, "pular" : 4, "volume" : 5, "pausa" : 2}
print(tokens_musica.get('volume'))


class interprete:
    def interpretar(texto):
        n1 = []
        for palavra in palavraschave:
            if palavra in texto:
              n1.append(palavraschave.index(palavra))
            else:
                pass
        print(n1)


    def atividade (self, num_atividade, *args):




# interprete.interpretar(p)






