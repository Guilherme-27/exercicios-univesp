from tkinter import Tk, Button
from tkinter.messagebox import showinfo
from time import strftime, localtime, gmtime

'Implemente um aplicativo GUI que contenha dois botões rotulados “Hora local” e “Hora de Greenwich”.'

def gmt():
    'exibe informação de dia e hora gmt'
    hora = strftime('Dia: %d %b %Y \nHora: %H:%M:%S %p\n', gmtime())
    showinfo(message=hora)

def local():
    'exibe informação de dia e hora local'
    hora = strftime('Dia: %d %b %Y \nHora: %H:%M:%S %p\n', localtime())
    showinfo(message=hora)
    
raiz = Tk()
hora_local = Button(raiz, text='Hora local', command=local)
hora_local.pack(expand=1, padx=10, pady=10)
hora_gmt = Button(raiz, text='Hora GMT', command=gmt)
hora_gmt.pack(expand=1, padx=10, pady=10)
raiz.mainloop()