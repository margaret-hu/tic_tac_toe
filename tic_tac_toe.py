from tkinter import *
from tkinter import messagebox

root = Tk()
board = []
for r in range(3):
    row_list = []
    for c in range(3):
        b = Button(root, text=" ", bg="ivory", width=5, command=lambda _r=r, _c=c: pick(_r, _c))
        row_list.append(b)
        b.grid(row=r, column=c)
    board.append(row_list)

current = "x"
def pick(r, c):
    global current
    button = board[r][c]
    sel = button["text"]
    if not (sel == " "):
        print("already occupied by", sel, ": move ignored")
        return
    button["text"] = current
    has_winner = check_win(r, c)
    print("has_winner is", has_winner)
    if has_winner:
        answer = messagebox.askyesno("need your input", current + " wins, new game?")
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
    a = board[1][1]["text"] # the diagonal
    if a == " ":
        return False
    if board[0][0]["text"] == a == board[2][2]["text"]:
        return True
    if board[0][2]["text"] == a == board[2][0]["text"]:
        return True
    return False

root.mainloop()
