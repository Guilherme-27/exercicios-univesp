from tkinter import Tk, Label
#teste simples
raiz = Tk()
hello = Label(master=raiz, text= "Hello, world")
hello.pack() #se nenhum argumento for passado, hello é colocado na posição padrão: centralizado e contra o limite superior do master
raiz.mainloop()