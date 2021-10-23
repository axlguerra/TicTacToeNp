import tkinter
from tkinter import messagebox
import numpy as np


window = tkinter.Tk()

window.title('Tic Tac Toe')

#X STARTS SO TRUE
clicked = True
count = 0


#Functions


def dissable_all_buttons():
    buttons=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
    for button in buttons:
        button.config(state=tkinter.DISABLED)

def turn_red(*args):
    for arg in args:
        arg.config(bg='red')


def checkifwinmatrix():
    global winner
    winner = False


    for row in matrix:
        #Horizontal conditions
        if row[0]['text'] == 'X' and row[1]['text'] == 'X' and row[2]['text'] == 'X':

            turn_red(row[0], row[1], row[2])

            tkinter.messagebox.showinfo('TicTacToe', 'Congratulations, X Won')

            dissable_all_buttons()


        elif row[0]['text'] == 'O' and row[1]['text'] == 'O' and row[2]['text'] == 'O':

            turn_red(row[0], row[1], row[2])

            messagebox.showinfo('TicTacToe', 'Congratulations, O Won')

            dissable_all_buttons()

        #vertical contidions
        if count == 9 and winner == False:

            messagebox.showinfo('TicTacToe', 'Its a tie, reset the game')

            dissable_all_buttons()

def check_columns():
    inv_matrx = matrix.transpose()
    # Horizontal conditions
    for row in inv_matrx:

        if row[0]['text'] == 'X' and row[1]['text'] == 'X' and row[2]['text'] == 'X':

            turn_red(row[0], row[1], row[2])

            tkinter.messagebox.showinfo('TicTacToe', 'Congratulations, X Won')

            dissable_all_buttons()


        elif row[0]['text'] == 'O' and row[1]['text'] == 'O' and row[2]['text'] == 'O':

            turn_red(row[0], row[1], row[2])

            messagebox.showinfo('TicTacToe', 'Congratulations, O Won')

            dissable_all_buttons()


def check_diagonals():
    diagonal = matrix.diagonal()
    inv_matrix = np.fliplr(matrix)

    inv_diagonal = inv_matrix.diagonal()



    if diagonal[0]['text'] == 'X' and diagonal[1]['text'] == 'X' and diagonal[2]['text']=='X':
        turn_red(diagonal[0], diagonal[1], diagonal[2])
        messagebox.showinfo('TicTacToe', 'Congratulations, X WON!')

    elif diagonal[0]['text'] == 'O' and diagonal[1]['text'] == 'O' and diagonal[2]['text']=='O':
        turn_red(diagonal[0], diagonal[1], diagonal[2])
        messagebox.showinfo('TicTacToe', 'Congratulations, O WON!')

    elif inv_diagonal[0]['text'] == 'X' and inv_diagonal[1]['text'] == 'X' and inv_diagonal[2]['text']=='X':
        turn_red(inv_diagonal[0], inv_diagonal[1], inv_diagonal[2])
        messagebox.showinfo('TicTacToe', 'Congratulations, X WON!')

    elif inv_diagonal[0]['text'] == 'O' and inv_diagonal[1]['text'] == 'O' and inv_diagonal[2]['text']=='O':
        turn_red(inv_diagonal[0], inv_diagonal[1], inv_diagonal[2])
        messagebox.showinfo('TicTacToe', 'Congratulations, O WON!')



#
# def checkifwin():
#     global winner
#     winner = False
#
#     if b1['text'] == 'X' and b2['text'] == 'X' and b3['text']=='X':
#         turn_red(b1,b2,b3)
#         tkinter.messagebox.showinfo('TicTacToe', 'Congratulations, X Won')
#         dissable_all_buttons()
#     elif b4['text'] == 'X' and b5['text'] == 'X' and b6['text']=='X':
#         turn_red(b4, b5, b6)
#
#         tkinter.messagebox.showinfo('TicTacToe', 'Congratulations, X Won')
#         dissable_all_buttons()
#     elif b7['text'] == 'X' and b8['text'] == 'X' and b9['text']=='X':
#         turn_red(b7, b8, b9)
#         tkinter.messagebox.showinfo('TicTacToe', 'Congratulations, X Won')
#         dissable_all_buttons()
#     elif b1['text'] == 'X' and b4['text'] == 'X' and b7['text']=='X':
#         turn_red(b1, b4, b7)
#         tkinter.messagebox.showinfo('TicTacToe', 'Congratulations, X Won')
#         dissable_all_buttons()
#     elif b2['text'] == 'X' and b5['text'] == 'X' and b8['text']=='X':
#         turn_red(b2, b5, b8)
#         tkinter.messagebox.showinfo('TicTacToe', 'Congratulations, X Won')
#         dissable_all_buttons()
#     elif b3['text'] == 'X' and b6['text'] == 'X' and b9['text']=='X':
#         turn_red(b3, b6, b9)
#         tkinter.messagebox.showinfo('TicTacToe', 'Congratulations, X Won')
#         dissable_all_buttons()
#     elif b1['text'] == 'X' and b5['text'] == 'X' and b9['text']=='X':
#         turn_red(b1, b5, b9)
#         tkinter.messagebox.showinfo('TicTacToe', 'Congratulations, X Won')
#         dissable_all_buttons()
#     elif b3['text'] == 'X' and b5['text'] == 'X' and b7['text']=='X':
#         turn_red(b3, b5, b7)
#         tkinter.messagebox.showinfo('TicTacToe', 'Congratulations, X Won')
#         dissable_all_buttons()
#
#     # Check for 'O'
#     elif b1['text'] == 'O' and b2['text'] == '0' and b3['text']=='O':
#         turn_red(b1,b2,b3)
#         tkinter.messagebox.showinfo('TicTacToe', 'Congratulations, O Won')
#         dissable_all_buttons()
#     elif b4['text'] == 'O' and b5['text'] == 'O' and b6['text']=='O':
#         turn_red(b4,b5,b6)
#         tkinter.messagebox.showinfo('TicTacToe', 'Congratulations, 0 Won')
#         dissable_all_buttons()
#     elif b7['text'] == '0' and b8['text'] == '0' and b9['text']=='O':
#         turn_red(b7,b8,b9)
#         tkinter.messagebox.showinfo('TicTacToe', 'Congratulations, 0 Won')
#         dissable_all_buttons()
#     elif b1['text'] == 'O' and b4['text'] == 'O' and b7['text']=='O':
#         turn_red(b1,b4,b7)
#         tkinter.messagebox.showinfo('TicTacToe', 'Congratulations, 0 Won')
#         dissable_all_buttons()
#     elif b2['text'] == 'X' and b5['text'] == 'X' and b8['text']:
#         turn_red(b2,b5,b8)
#         tkinter.messagebox.showinfo('TicTacToe', 'Congratulations, 0 Won')
#         dissable_all_buttons()
#     elif b3['text'] == 'O' and b6['text'] == 'O' and b9['text']=='O':
#         turn_red(b3,b6,b9)
#         tkinter.messagebox.showinfo('TicTacToe', 'Congratulations, 0 Won')
#         dissable_all_buttons()
#     elif b1['text'] == 'O' and b5['text'] == 'O' and b9['text']=='O':
#         turn_red(b1,b5,b9)
#         tkinter.messagebox.showinfo('TicTacToe', 'Congratulations, 0 Won')
#         dissable_all_buttons()
#     elif b3['text'] == 'O' and b5['text'] == 'O' and b7['text']=='O':
#         turn_red(b3,b5,b7)
#         tkinter.messagebox.showinfo('TicTacToe', 'Congratulations, 0 Won')
#         dissable_all_buttons()


def b_clicked(b):
    global clicked, count

    if b['text'] == '_' and clicked == True:
        b['text']= 'X'
        clicked = False
        count +=1
        # checkifwin()
        checkifwinmatrix()
        check_columns()
        check_diagonals()
    elif b['text'] == '_' and clicked == False:
        b['text'] = 'O'
        clicked = True
        count +=1
        # checkifwin()
        checkifwinmatrix()
        check_columns()
        check_diagonals()


    else:
        messagebox.showerror('TicTacToe', 'Hey that Box has already been selected')


#Buttons
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, clicked, count, matrix
    clicked=True
    count = 0

    b1 = tkinter.Button(window, text='_', font=('Helvetica', 20), height=3, width=6, bg='SystemButtonFace', command=lambda: b_clicked(b1))
    b2 = tkinter.Button(window, text='_', font=('Helvetica', 20), height=3, width=6, bg='SystemButtonFace', command=lambda: b_clicked(b2))
    b3 = tkinter.Button(window, text='_', font=('Helvetica', 20), height=3, width=6, bg='SystemButtonFace', command=lambda: b_clicked(b3))
    b4 = tkinter.Button(window, text='_', font=('Helvetica', 20), height=3, width=6, bg='SystemButtonFace', command=lambda: b_clicked(b4))
    b5 = tkinter.Button(window, text='_', font=('Helvetica', 20), height=3, width=6, bg='SystemButtonFace', command=lambda: b_clicked(b5))
    b6 = tkinter.Button(window, text='_', font=('Helvetica', 20), height=3, width=6, bg='SystemButtonFace', command=lambda: b_clicked(b6))
    b7 = tkinter.Button(window, text='_', font=('Helvetica', 20), height=3, width=6, bg='SystemButtonFace', command=lambda: b_clicked(b7))
    b8 = tkinter.Button(window, text='_', font=('Helvetica', 20), height=3, width=6, bg='SystemButtonFace', command=lambda: b_clicked(b8))
    b9 = tkinter.Button(window, text='_', font=('Helvetica', 20), height=3, width=6, bg='SystemButtonFace', command=lambda: b_clicked(b9))
    matrix = np.array([[b1, b2, b3], [b4, b5, b6], [b7, b8, b9]])




#Grid
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

#Menu
my_menu = tkinter.Menu(window)
window.config(menu=my_menu)
options_menu = tkinter.Menu(my_menu, tearoff=False)
my_menu.add_cascade(labe='Options', menu=options_menu)
options_menu.add_command(label='Reset Game', command=reset)
reset()

tkinter.mainloop()