from tkinter import *
from board_gen import main as bg
import numpy as np
import time

window = Tk()

ROW, COL = 15, 15

board, start, end = bg((ROW, COL))


np_arr = [0 if x == "*" else 2 if x == "X" else 1 for x in board.values()]


arr = np.array(np_arr).reshape((15, 15))
arr_old = arr.copy()
arr_old[start][end] = 5

results = []


# Inspiration from: https://www.101computing.net/backtracking-maze-path-finder/
def backtracker(board, i, j, results):
    if board[i][j] == 2:
        results.append([(i, j), 2])
        return True

    elif board[i][j] == 1:

        board[i][j] = 3
        results.append([(i, j), 3])

        if i < len(board) - 1 and backtracker(board, i + 1, j, results):
            return True
        if i > 0 and backtracker(board, i - 1, j, results):
            return True

        if j < len(board[0]) and backtracker(board, i, j + 1, results):
            return True

        if j > 0 and backtracker(board, i, j - 1, results):
            return True

        results.append([(i, j), 4])
        board[i][j] = 4


my_dict = {}


def get_color(loca_value):
    if loca_value == 0:
        return "black"
    if loca_value == 1:
        return "red"
    if loca_value == 2:
        return "green"
    if loca_value == 5:
        return "blue"
    if loca_value == 3:
        return "purple"
    if loca_value == 4:
        return "gray"


def create_labels():
    for x in range(ROW):
        for y in range(COL):

            value = arr_old[x][y]

            # If using textvariable as the label text
            # a_key = StringVar()
            # a_key.set(str(value))

            my_label = Label(
                window, textvariable="", bg=get_color(value), relief=RIDGE, width=5
            )
            my_label.grid(row=x, column=y)

            my_dict[(x, y)] = my_label


def after_runner():

    for x in results:
        my_dict[x[0]].config(bg=get_color(x[1]))
        window.update_idletasks()
        time.sleep(0.1)


backtracker(arr, start, end, results)
create_labels()
window.after(2000, after_runner)
window.mainloop()
