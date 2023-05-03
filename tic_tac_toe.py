from tkinter import *
from tkinter import messagebox
import tkinter.font as font

root = Tk()
root.wm_title("Tic Tac Toe")
board = []
for r in range(3):
    row_list = []
    for c in range(3):
        b = Button(root, text=" ", bg="ivory", width=5, height=3, command=lambda _r=r, _c=c: pick(_r, _c))
        b['font'] = font.Font(size=20)
        row_list.append(b)
        b.grid(row=r, column=c)
    board.append(row_list)

current = "x"


def pick(r, c):
    global current
    button = board[r][c]
    select = button["text"]
    if not (select == " "):
        return
    button["text"] = current
    has_winner = check_win(r, c)
    if has_winner:
        answer = messagebox.askyesno("Game Over", current + " wins, new game?")
        if answer == True:
            for r in range(3):
                for c in range(3):
                    board[r][c]["text"] = " "
        else:
            exit()
    current = "o" if current == "x" else "x"


def check_win(r, c):
    if board[r][0]["text"] == board[r][1]["text"] == board[r][2]["text"]:
        return True
    if board[0][c]["text"] == board[1][c]["text"] == board[2][c]["text"]:
        return True
    a = board[1][1]["text"]  # the diagonal
    if a == " ":
        return False
    if board[0][0]["text"] == a == board[2][2]["text"]:
        return True
    if board[0][2]["text"] == a == board[2][0]["text"]:
        return True
    return False


root.mainloop()
