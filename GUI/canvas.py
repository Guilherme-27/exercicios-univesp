from tkinter import Tk, Canvas
	
# manipuladores de evento
def begin(event):
    'inicializa o início da curva com a posição do mouse '

    global oldx, oldy
    oldx, oldy = event.x, event.y

def draw(event):
    'desenha um segmento de linha da posição antiga do mouse à nova'
    global oldx, oldy, canvas
    newx, newy = event.x, event.y # nova posição do mouse

    # conecta posição anterior do mouse à atual
    canvas.create_line(oldx, oldy, newx, newy)

    oldx, oldy = newx, newy # conecta posição anterior do mouse à atual

root = Tk()

oldx, oldy = 0, 0   # coordenadas do mouse (variáveis globais)
	
# canvas
canvas = Canvas(root, height=100, width=150)

# vincula evento de clique do botão esquerdo à função begin()
canvas.bind('<Button-1>', begin)

# vincula evento de movimento do mouse enquanto o botão está pressionado
canvas.bind('<Button1-Motion>', draw)

canvas.pack()
root.mainloop()