#Para simplificar a especificação da geometria, 
# podemos usar um widget Frame cuja única finalidade é ser o 
# master dos outrs widgets

from tkinter import Tk, Canvas, Frame, Button, SUNKEN, LEFT, RIGHT

# manipuladores de evento up(), down(), left() e right()

def up():
    'move a caneta 10 pixels para cima'
    global y, canvas
    canvas.create_line(x,y, x, y-10)
    y -= 10

def down():
    'move a caneta 10 pixels para baixo'
    global y, canvas
    canvas.create_line(x,y, x, y+10)
    y += 10

def left():
    'move a caneta 10 pixels para esquerda'
    global x, canvas
    canvas.create_line(x,y, x-10, y)
    x -= 10

def right():
    'move a caneta 10 pixels para direita'
    global x, canvas
    canvas.create_line(x, y, x+10, y)
    x += 10

root = Tk()
# tela com borda de tamanho 100 x 150
canvas = Canvas(root, height=100, width=150, relief=SUNKEN, borderwidth=3)
canvas.pack(side=LEFT)


# frame para manter os 4 botões
box = Frame(root)
box.pack(side=RIGHT)

# os 4 widgets de botão têm a caixa do widget Frame como seu master
button = Button(box, text='up', command=up)
button.grid(row=0, column=0, columnspan=2)
button = Button(box, text='left', command=left)
button.grid(row=1, column=0)
button = Button(box, text='right', command=right)
button.grid(row=1, column=1)
button = Button(box, text='down', command=down)
button.grid(row=2, column=0, columnspan=2)

x,y = 50, 75 # posição da caneta, inicialmente no meio

root.mainloop()