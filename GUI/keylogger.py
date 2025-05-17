from tkinter import Tk, Text

def record(event):
    '''função de manipulação de evento para evento de tecla pressionada
    evento de entrada é do tipo tkinter.Event '''
    print(f'char = {event.keysym}')


root = Tk()

#widget texto
text = Text(root, width=20, height=5)

# Vincula evento de tecla à função de tratamento de evento record()
text.bind('<KeyPress>', record)

# widget expande se master também expandir
text.pack(expand=True, fill='both')




root.mainloop()