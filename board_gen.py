from typing import Tuple
import random as rnd



# Print for helping purposes
def print_debug(board: dict, rows: int, columns: int) -> None:
    temp_list = list(board.values())
    chunks = [temp_list[x:x+columns] for x in range(0, len(temp_list), columns)]
    for chunk in chunks:
        print("".join(chunk)+"\n")



def insert_walls(board):

    max_walls = round(len([x for x in board.values() if x != "*"])*0.6, 0)
    min_walls = round(len([x for x in board.values() if x != "*"])*0.3, 0)

    walls = rnd.randint(min_walls, max_walls)
    
    start_x, start_y = -1,-1
    
    while True:
        i, j, k, l = rnd.randint(1, 13), rnd.randint(1, 13), rnd.randint(1, 13), rnd.randint(1, 13)
        if i != k or j != l:
            board[(i,j)] = "X"
            board[(k, l)] = "S"
            start_x, start_y = k,l
            break
        

    counter = 0
    while counter < walls:
        i, j = rnd.randint(1, 13), rnd.randint(1, 13)
        
        if board[(i,j)] != "*" and board[(i,j)] != "X" and board[(i,j)] != "S":
            board.update({(i, j): "*"})        
            counter += 1
    
    return start_x, start_y
    
def main(size: Tuple[int, int]) -> dict:

    # Initialize dict with correct keys
    rows, columns = size 
    board = {(i,j): " " for i in range(rows) for j in range(columns)}

    board.update({(i,j): "*" for i in range(rows) for j in range(columns) if i == 0 or i == rows-1 or j == 0 or j == columns-1})

    start_x, start_y = insert_walls(board)
    
    print_debug(board, 15, 15)

    return board, start_x, start_y
