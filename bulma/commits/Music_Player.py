from tkinter import *
from tkinter import font
import pygame
import random
import os
from tkinter.filedialog import askdirectory
import threading
'''
    Programa para tocar musicas
'''

def escolher_volume():
    global volume
    x = "a"
    while True:
        y = volumeBar.get()/100

        if y != x:
            pygame.mixer.music.set_volume(volumeBar.get()/100)
        x = y



# Menu Defs
def abrir():
    global musicas, lista, x

    diretorio = askdirectory()
    for file in os.listdir(diretorio):
        ext = file.rfind(".")
        if file[ext:] in EXTENSOES:
            if (diretorio + "/" + str(file)) not in musicas:
                musicas.append(diretorio + "/" + str(file))
                print(diretorio)
    for musica in musicas:
        começo = musica.rfind("/")
        final = musica.rfind(".")
        if musica[começo+1: final] not in adicionadas:
            x += 1
            lista.insert(x, musica[começo+1: final])
    for a in lista.get(0, END):
        if a not in adicionadas:
            adicionadas.append(a)

def load():
    pass
    '''global adicionadas, musicas
    loadFile = open("save.txt", "r")
 
    loadFile.close()'''

def salvar():
    global adicionadas, musicas
    saveFile = open("save.txt", "w+")
    saveFile.write(str(adicionadas)+"\n")
    saveFile.write(str(musicas))
    saveFile.close()

    print('salvo')

# Button Defs
def play(index = 0):
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
    index=adicionadas.index(random.choice(adicionadas))
    lista.select_clear(0, END)
    lista.select_set(index)
    pygame.mixer.music.load(musicas[index])
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()

# Pygame


# Variaveis e constantes
x = 0
vai = False
volume = 1
adicionadas = []
musicas = []
BACKGROUND = "#92f2da"
EXTENSOES = [".mp3", ".mp4"]

# Janela
janela = Tk()
janela.geometry('700x550')
janela.title("Music Player, por Joaninha ;D")

menu = Menu(janela)
janela.config(background=BACKGROUND, menu=menu)
fonte_pequena = font.Font(janela, size=15)

# Menu
arquivos = Menu(menu, tearoff=0)
menu.add_cascade(label="Arquivos", menu=arquivos)
arquivos.add_command(label="abrir", command=abrir)
arquivos.add_command(label="salvar", command=salvar)
arquivos.add_command(label="carregar", command=load)
arquivos.add_separator()
arquivos.add_command(label="sair", command=quit)

# Lista
lista = Listbox(janela, font=fonte_pequena, width=22, bg="#cdf9ee")
lista.config(height=lista.size())
lista.grid(row=0, column=0)

# Escala
volumeBar = Scale(janela,
                              from_=0,
                              to=100,
                              )
volumeBar.place(x=lista.winfo_reqwidth(), y=0)

# Botoes
play = Button(janela, text='Play', font=fonte_pequena, width=7, command=play)
pause = Button(janela, text='Pause', font=fonte_pequena, width = 7, command=pause)
resume = Button(janela, text='Resume', font=fonte_pequena, width = 7, command=resume)
aleatoria = Button(janela, text='Random', font=fonte_pequena, width = 7, command=aleatoria)
play.place(x=700-play.winfo_reqwidth(), y=0)
pause.place(x=700-pause.winfo_reqwidth(), y=play.winfo_reqheight())
resume.place(x=700-resume.winfo_reqwidth(), y=play.winfo_reqheight()+pause.winfo_reqheight())
aleatoria.place(x=700-aleatoria.winfo_reqwidth(), y=play.winfo_reqheight()+pause.winfo_reqheight()+resume.winfo_reqheight())


func1 = threading.Thread(target=escolher_volume, args=())
func1.start()
janela.mainloop()
