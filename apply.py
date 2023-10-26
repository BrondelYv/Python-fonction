
from CSVtoXML import CSVtoXML as ctx
from CSVtoJSON import CSVtoJSON as ctj
from XMLtoCSV import XMLtoCSV as xtc
from XMLtoJSON import XMLtoJSON as xtj

ctx(outputfile='rso.xml', inputfile='database_FAF1.csv')
ctj('database_FAF1.csv', 'database_FAF1.json')
xtc('database_FAF1.xml', 'database_FAF1.csv')
xtj('database_FAF1.xml', 'database_FAF1.json')


"""
from tkinter import *

import webbrowser


def open_transformer_extension():
    webbrowser.open_new('https://incitius.com/')


# creer une premiere fenetre
window = Tk()

# personnaliser cette fenetre
window.title("My Tools")
window.geometry("")
window.minsize(480, 360)
window.iconbitmap("logo.jpg")
window.config(background="#41B77F")

# creer un frame
frame = Frame(window, bg='#41B77F')


# ajouter un premier texte
label_title = Label(frame, text='Welcome on ExtensionTransform', font="Courrier, 20", bg='#41B77F', fg='black')
label_title.pack()

# ajouter un second texte
label_subtitle = Label(frame, text='Put your file name extension', font="Courrier, 13", bg='#41B77F', fg='black')
label_subtitle.pack()

# ajouter un premier bouton
yt_button = Button(frame, text='Opening', font="Courrier, 15", bg='black', fg='#41B77F', command=open_transformer_extension)
yt_button.pack()

# ajouter
frame.pack(expand=YES)


# afficher
window.mainloop()
"""