from tkinter import *
import threading
from tkinter import messagebox
import tkinter as tk
import social
from tkinter import font

class Passwords:


    def __init__(self):
        self.frame1 = Frame()


        Label(text='piada do dia', fg='darkblue',
              font=('Cross X', '26', 'bold'), height=1).pack()
        Label(text='compromissos',
              font=('Cross X', '26', 'bold'), height=1).pack()
        Label(text="***********************************", font=('fonte1'), width=15).pack()
        Label(text="***********************************", font=('fonte1'), width=15).pack()
#        self.nome.focus_force()  # Para o foco começar neste campo
        Label(text='compromissos',
              font=('Cross X', '26', 'bold'), height=1).pack()

















"""    def conferir(self):
        NOME=self.nome.get()
        SENHA=self.senha.get()
        if NOME == SENHA:
            self.msg['text']='ACESSO PERMITIDO'
            self.msg['fg']='darkgreen'
        else:
            self.msg['text']='ACESSO NEGADO'
            self.msg['fg']='red'
            self.nome.focus_force()"""
