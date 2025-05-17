from tkinter import END, Tk, Label, Button, Entry
from tkinter.messagebox import showinfo
from time import strftime, strptime


def compute():
    '''exibe dia da semana correspondente à data em date_entry 
    data deve ter formato MMM DD, AAAA (ex.: Jan 21, 1967)'''

    global date_entry

    date = date_entry.get()

    # calcula dia da semana correspondente à data
    weekday = strftime('%A', strptime(date, '%b %d, %Y'))
    
    showinfo(message= f'{date} was {weekday}')

    date_entry.delete(0, END)

raiz = Tk()

#label
label = Label(raiz, text='Digite a data')
label.grid(row=0, column=0, padx=10, pady=10)

#data_entry
date_entry = Entry(raiz)
date_entry.grid(row=1, column=0, padx=10, pady=10)

#button
botao = Button(raiz, text='Inserir', command=compute)
botao.grid(row=2, column=0, padx=10, pady=10)



raiz.mainloop()