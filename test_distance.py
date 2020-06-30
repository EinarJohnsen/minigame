from tkinter import *
import random


from board_gen import main as bg
import numpy as np
from sklearn.utils.graph import single_source_shortest_path_length
import time

window = Tk()

board, start, end = bg((15, 15))


np_arr = [0 if x == "*" else 2 if x == "X" else 1 for x in board.values()]


arr = np.array(np_arr).reshape((15,15))

#arr[start][end] = 1

arr_old = arr.copy()
arr_old[start][end] = 5

results = {}

# Inspiration from: https://www.101computing.net/backtracking-maze-path-finder/

def backtracker(board, i, j, results):
    
    print(board, i, j, results)
    
    print(board[i][j])
    
    if board[i][j] == 2:
        results[(i,j)] = 2
        print("we done")
        print(board)
        return True
    
    elif board[i][j] == 1:
        
        board[i][j] = 3
        results[(i,j)] = 3

        if i < len(board)-1 and backtracker(board, i+1, j, results):
            return True
        if i > 0 and backtracker(board, i-1, j, results):
            return True
        
        if j < len(board[0]) and backtracker(board, i, j+1, results):
            return True
        
        if j > 0 and backtracker(board, i, j-1, results):
            return True
        
        results[(i,j)] = 4
        board[i][j] = 4 
        print("pop - backtrack")


#print(start, end)
backtracker(arr, start, end, results)
print(start, end)
print(results)

#colours = ['red','green','orange','white','yellow','blue']
#my_dict = {f"{x}_{y}":x*y for x in range(15) for y in range(15)}

my_dict= {}


def get_color(value):
    if value == 0:
        return "black"
    if value == 1:
        return "red"
    if value == 2:
        return "green"
    if value == 5:
        return "blue"
    if value == 3:
        return "yellow"
    if value == 4:
        return "gray"

keys = []
for x in range(15):
    for y in range(15):

        value = arr_old[x][y]

        a_key = StringVar()
        a_key.set(str(value))

        my_label = Label(window, textvariable=a_key, bg=get_color(value), relief=RIDGE, width=5)
        my_label.grid(row=x, column=y)

        my_dict[(x,y)] = my_label


#print(my_dict)


def test(arr, start, end):
    print("--")
    print(arr, start, end)
    print("test")

def after_runner():

    
    #if flag:
    
    for x in results:
        my_dict[x].config(bg=get_color(results[x]))
        window.update_idletasks()
        time.sleep(0.1)
    
    #time.sleep(1)
    #print(arr)
    #print(start)
    #print(end)



    #print("done")

    
    #window.update_idletasks()



    #tk.Label(textvar=str(random.randint(1, 100)),bg="red", width=5).grid(row=10, column=10)

    #for x in range(10):
    #    for y in range(10):
    #        
    #        #time.sleep(1)



#window.after(5000, after_runner())
#after_runner()
window.after(2000, after_runner)
window.mainloop()
#after_runner()








#r = 0
#for c in colours:
#    tk.Label(text=c, bg=c, relief=tk.RIDGE, width=10).grid(row=r,column=0)
#    r = r + 1

#l1 = tk.Label(text="Test", fg="black", bg="white")
