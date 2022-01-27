from tkinter import *
from tkinter import font
import pygame
import random
import os
from tkinter.filedialog import askdirectory
import threading
class player():
    def __init__(self):
        # Variaveis e constantes
        self.x = 0
        self.vai = False
        self.volume = 1
        self.adicionadas = []
        self.musicas = []
        self.BACKGROUND = "#2d6572"
        self.EXTENSOES = [".mp3", ".mp4"]

        # Janela

        self.janela = Tk()
        self.janela.geometry('450x300')
        self.janela.title("Music Player, por Joaninha ;D")
        self.menu = Menu(self.janela)
        self.janela.config(background=self.BACKGROUND, menu=self.menu)
        self.fonte_pequena = self.font=('Cross X', '10', 'bold')

        def abrir():
            global musicas, lista, x

            playlist = "C:/Users/Lucas Gabriel/Music/Makalister - Laura Müller Mixtape"
            diretorio = askdirectory()

            for file in os.listdir(playlist):
                ext = file.rfind(".")
                if file[ext:] in self.EXTENSOES:
                    if (diretorio + "/" + str(file)) not in musicas:
                        musicas.append(diretorio + "/" + str(file))
                        print(diretorio)
            for musica in musicas:
                comeco = musica.rfind("/")
                final = musica.rfind(".")
                if musica[comeco + 1: final] not in adicionadas:
                    x += 1
                    lista.insert(x, musica[comeco + 1: final])
            for a in lista.get(0, END):
                if a not in adicionadas:
                    adicionadas.append(a)

        playlists = [[1, 2, 3, 4],
                     coito := {
                         'primor': 'a mais especial',
                         'atrevida': 'safadones',
                         'insaciável': 'a mais +',
                         'sempre': 'basica',
                         'lírico': 'fofors'
                     },
                     rap := {
                         'makalister': "sad",
                         'djonga': 'todas',
                         'antigas': 'self kk',
                         'novas': 'pqp',
                         'trap': 'praqtudum',
                         'dudu': ' acidia',
                         'recente': 'boora'
                     },
                     djonga := {
                         'nu': "sd",
                         'ladrao': 'kl',
                         'todas': 'f'
                     },
                     mpb := {
                         'seujorge': 'sd'
                     }
                     ]

        def escolher_volume():
            global volume
            x = "a"
            while True:
                y = volumeBar.get() / 100

                if y != x:
                    pygame.mixer.music.set_volume(volumeBar.get() / 100)
                x = y

        def salvar():
            global adicionadas, musicas
            saveFile = open("save.txt", "w+")
            saveFile.write(str(adicionadas) + "\n")
            saveFile.write(str(musicas))
            saveFile.close()

            print('salvo')

        # Button Defs
        def play(index=0):
            global volume
            if index == 0:
                index = adicionadas.index(lista.get(lista.curselection()))

            pygame.mixer.music.load(musicas[index])
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play()

        def pause():
            pygame.mixer.music.pause()

        def resume():
            pygame.mixer.music.unpause()

        def aleatoria():
            global adicionadas
            index = adicionadas.index(random.choice(adicionadas))
            lista.select_clear(0, END)
            lista.select_set(index)
            pygame.mixer.music.load(musicas[index])
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play()

        # Menu
        self.arquivos = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Arquivos", menu=self.arquivos)
        self.arquivos.add_command(label="abrir", command=abrir)
        self.arquivos.add_command(label="salvar", command=salvar)
        self.arquivos.add_separator()
        self.arquivos.add_command(label="sair", command=quit)


        # Lista
        self.lista = Listbox(self.janela, font=self.fonte_pequena, width=22, bg="#e0b0b5")
        self.lista.config(height=self.lista.size())
        self.lista.grid(row=0, column=0)

        # Escala
        self.volumeBar = Scale(self.janela,
                                      from_=0,
                                      to=100,
                                      )
        self.volumeBar.place(x=self.lista.winfo_reqwidth(), y=0)
        self.fonte_braba = self.font=('Cross X', '26', 'bold')
        # Botoes
        self.play = Button(self.janela, text='Play', font=self.fonte_pequena, width=7, command=play, bg='#b87044')
        self.pause = Button(self.janela, text='Pause', font=self.fonte_pequena, width = 7, command=pause, bg='#b87044')
        self.resume = Button(self.janela, text='Resume', font=self.fonte_pequena, width = 7, command=resume, bg='#b87044')
        self.aleatoria = Button(self.janela, text='Random', font=self.fonte_pequena, width = 7, command=aleatoria, bg='#b87044')
        self.exit = Button(self.janela, text='sair', font=self.fonte_pequena, width = 7, command=quit, bg='#b87044')
        self.lanzar = Button(self.janela, text = 'lanzar a braba', font=self.fonte_braba, width = 15, command=abrir, bg='#b87044')
        self.play.place(x=450-self.play.winfo_reqwidth(), y=0)
        self.pause.place(x=450-self.pause.winfo_reqwidth(), y=self.play.winfo_reqheight())
        self.resume.place(x=450-self.resume.winfo_reqwidth(), y=self.play.winfo_reqheight()+self.pause.winfo_reqheight())
        self.aleatoria.place(x=450-self.aleatoria.winfo_reqwidth(), y=self.play.winfo_reqheight()+self.pause.winfo_reqheight()+self.resume.winfo_reqheight())
        self.exit.place(x=450-self.aleatoria.winfo_reqwidth(), y=self.play.winfo_reqheight()+self.pause.winfo_reqheight()+self.resume.winfo_reqheight()+self.aleatoria.winfo_reqheight())
        self.lanzar.place(x=50, y=200)










