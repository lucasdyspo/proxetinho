import googlesearch
import speech_recognition as sr
import pyttsx3
import json
# import pyaudio
from teste import prepare_data
import numpy as np
from tkinter import *
import threading
from tkinter import messagebox
import tkinter as tk
import social
from tkinter import font
from exemlos import Passwords
from musicas import player

try:
    from googlesearch import search
except:
    print("googlesearch not imported!")
googlesearch = True

with open("intents.json") as file:
    data = json.load(file)

def speak(text):
    speaker = pyttsx3.init()
    speaker.say(text)
    speaker.runAndWait()


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            text = r.recognize_google(audio, language='pt-BR')
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return text

# tags = []  # Contains all the different tags
# all_questions_list = []  # Contains the different question with their words tokenized
# questions_tags = []  # Contains the questions tags corresponding to the questions in above list
# all_question_words = []  # Contains all the words in all the questions of the dataset
#
# pr = prepare_data(data)
# all_question_words, tags, all_questions_list, questions_tags = pr.prepare(data, "intents", "all_questions", "tag")
#
# all_questions_train = []
# tags_output = []
#
# all_questions_train, tags_output = pr.get_training_set()
# all_questions_train = np.array(all_questions_train)
# tags_output = np.array(tags_output)
#
#
# # Preparing sub tags models
# sub_tags_list = []
# sub_tags_models = []



#
# for intent in data["intents"]:
#     all_words_sub_questions = []
#     all_sub_tags = []
#     sub_question_tags = []
#     all_sub_questions_list = []
#
#     tr = prepare_data(data)
#     all_words_sub_questions, all_sub_tags, all_sub_questions_list, sub_question_tags = tr.prepare(intent, "sub_tags",
#                                                                                                   "questions", "sub")
#
#     all_sub_questions_train = []
#     sub_tags_output = []
#     all_sub_questions_train, sub_tags_output = tr.get_training_set()
#     all_sub_questions_train = np.array(all_sub_questions_train)
#     sub_tags_output = np.array(sub_tags_output)
#
#
#
#     sub_tags_list.extend(all_sub_tags)
#
# tags_dict = {}
# answers_dict = {}


def main():
    sentence = get_audio()

    msg_list.insert(tk.END, "You: " + sentence)
    if sentence.count("exit") > 0:
        msg_list.insert(tk.END, "Boss: Good Bye!")
        speak("Good bye")
        root.quit()

def wish():
    hour = int(datetime.datetime.now().hour)
    if 8 <= hour < 12:
        speak("bom dia né")
    elif 12 <= hour < 18:
        speak("tardezinha pique como")
    elif 2 > hour < 8:
        speak("madrugada, vilão, dorme")
    else:
        speak("de noite esquece ")

    speak("I am Boss sir, How can I help you")

def run():
    main_thread = threading.Thread(target=main)
    main_thread.start()

def msg_teste():
    messagebox.showinfo('fasd')






n = Tk()
n.title("BULMA")
n.config(bg="white")
n.geometry('900x690')
mic = PhotoImage(file='COPP.png')
botaomic=Button(n, text="não consigo vei", image =mic, border=0 ,command=lambda: player())
botaomic.pack()



Passwords()

n.mainloop()


"""root = tk.Tk()
root.geometry('500x600')
heading = tk.Label(root, text="Welcome! Press the Button and ask whatever you want!",
                   font=('montserrat', 12, "bold"), fg="black").pack()
frame = tk.Frame(root, bg="#FFF")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
your_msg = tk.StringVar()
y_scroll_bar = tk.Scrollbar(frame)
x_scroll_bar = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
msg_list = tk.Listbox(frame, height=20, width=50, yscrollcommand=y_scroll_bar.set, xscrollcommand=x_scroll_bar.set)
y_scroll_bar.pack(side=tk.RIGHT, fill=tk.Y, expand=tk.FALSE)
x_scroll_bar.pack(side=tk.BOTTOM, fill=tk.X, expand=tk.FALSE)
msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
msg_list.pack()
frame.pack()
"""




